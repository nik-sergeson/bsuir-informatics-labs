from __future__ import division
import logging

logging.basicConfig(level=logging.WARNING)


class ObjectWithID(object):
    _id = 0
    _local_id_start = 1

    def __init__(self):
        self.local_id = type(self).get_local_id()
        self.id = ObjectWithID._id
        ObjectWithID._id += 1

    @classmethod
    def get_local_id(cls):
        cls._id += 1
        return cls._id - 1


class DistributionParams(object):
    """
    :type param_names:list
    :type defargs:list
    :type defkwargs:dict
    """

    def __init__(self, param_names, *defargs, **defkwargs):
        self.param_names = param_names
        self.defargs = defargs
        self.defkwargs = defkwargs
        for param in param_names:
            if not param in self.defkwargs:
                self.defkwargs[param] = 0


class Application(ObjectWithID):
    _id = ObjectWithID._local_id_start

    def __init__(self, creation_time):
        super(Application, self).__init__()
        self.creation_time = creation_time
        self.service_finish_time = 0

    def set_service_finish_time(self, finish_time):
        self.service_finish_time = finish_time


class Channel(ObjectWithID):
    """
    :type distrib_params:DistributionParams
    """
    FREE, BUSY, BLOCKED = range(3)
    _name = "Channel"
    _id = ObjectWithID._local_id_start

    def __init__(self, time_distrib, distrib_params):
        super(Channel, self).__init__()
        self.condition = Channel.FREE
        self._raw_time_distrib = time_distrib
        self.service_end_time = 0
        self.start_time = 0
        self.distrib_params = distrib_params
        self.time_distrib = None
        self.application = None

    def set_distrib_params(self, from_view):
        kwargs = {}
        kwargs.update(self.distrib_params.defkwargs)
        kwargs.update(from_view)
        self.time_distrib = self._raw_time_distrib(*self.distrib_params.defargs, **kwargs)

    def service_completed(self, current_time):
        return current_time >= self.service_end_time

    def complete_service(self, current_time):
        if not self.service_completed(current_time):
            raise Exception("Service not completed")
        self.condition = Channel.FREE
        logging.info(
            "{} {} completed service,started at {} current time: {}".format(self._name, self.local_id, self.start_time,
                                                                            current_time))
        return self.application

    def start_service(self, current_time, application):
        if application is None:
            pass
        if not self.is_free():
            raise Exception("{} is not free".format(self._name))
        self.condition = Channel.BUSY
        self.service_end_time = current_time + self.time_distrib.rvs(size=1)[0]
        self.start_time = current_time
        self.application = application
        logging.info(
            "{} {} started service at {}, service will be completed at {}".format(self._name, self.local_id,
                                                                                  current_time,
                                                                                  self.service_end_time))

    def set_blocked(self):
        self.condition = Channel.BLOCKED
        logging.debug("{} {} is blocked".format(self._name, self.local_id))

    def is_free(self):
        return self.condition == Channel.FREE

    def is_busy(self):
        return self.condition == Channel.BUSY

    def is_blocked(self):
        return self.condition == Channel.BLOCKED

    def clear(self):
        self.condition = Channel.FREE
        self.service_end_time = 0
        self.start_time = 0
        self.time_distrib = None
        self.application = None


class ChannelWithStatistics(Channel):
    _id = ObjectWithID._local_id_start

    def __init__(self, time_distrib, distrib_params):
        super(ChannelWithStatistics, self).__init__(time_distrib, distrib_params)
        self.statistics = {Channel.FREE: 0, Channel.BUSY: 0, Channel.BLOCKED: 0}
        self.statistics[self.condition] = 1

    def complete_service(self, current_time):
        application = super(ChannelWithStatistics, self).complete_service(current_time)
        self.statistics[self.condition] += 1
        return application

    def start_service(self, current_time, application):
        super(ChannelWithStatistics, self).start_service(current_time, application)
        self.statistics[self.condition] += 1

    def set_blocked(self):
        super(ChannelWithStatistics, self).set_blocked()
        self.statistics[self.condition] += 1

    def get_probabilities(self):
        total_quantity = self.statistics[Channel.BLOCKED] + self.statistics[Channel.BUSY] + self.statistics[
            Channel.FREE]
        probs = {Channel.FREE: self.statistics[Channel.FREE] / total_quantity,
                 Channel.BUSY: self.statistics[Channel.BUSY] / total_quantity,
                 Channel.BLOCKED: self.statistics[Channel.BLOCKED] / total_quantity}
        return probs

    def clear(self):
        super(ChannelWithStatistics, self).clear()
        self.statistics = {Channel.FREE: 0, Channel.BUSY: 0, Channel.BLOCKED: 0}
        self.statistics[self.condition] = 1


class ApplicationReceiver(object):
    def __init__(self):
        super(ApplicationReceiver, self).__init__()

    def can_receive_application(self):
        return True

    def receive_application(self, current_time, application):
        pass


class ApplicationSender(object):
    def __init__(self):
        super(ApplicationSender, self).__init__()

    def take_application(self):
        pass


class EndStorage(ObjectWithID, ApplicationReceiver):
    """
    :type received_cache:list[Application]
    """
    _name = "EndStorage"
    _id = ObjectWithID._local_id_start

    def __init__(self):
        super(EndStorage, self).__init__()
        self.received_cache = []
        self.application_quantity = 0

    def _get_application(self):
        self.application_quantity -= 1
        return self.received_cache.pop(0)

    def _append_application(self, value):
        self.application_quantity += 1
        self.received_cache.append(value)

    def receive_application(self, current_time, application):
        application.set_service_finish_time(current_time)
        self._append_application(application)
        logging.info("{} {} have {} received applications".format(self._name, self.local_id, self.application_quantity))

    def clear(self):
        del self.received_cache[:]
        self.application_quantity = 0


class EndStorageStatistics(object):
    def __init__(self, end_storage):
        self.end_storage = end_storage

    def get_application_spacing(self):
        spacing = []
        for i in xrange(self.end_storage.application_quantity - 1):
            spacing.append(self.end_storage.received_cache[i + 1].service_finish_time - self.end_storage.received_cache[
                i].service_finish_time)
        return spacing

    def get_service_duraction(self):
        duraction = []
        for i in xrange(self.end_storage.application_quantity):
            duraction.append(self.end_storage.received_cache[i].service_finish_time - self.end_storage.received_cache[
                i].creation_time)
        return duraction


class Storage(ObjectWithID, ApplicationReceiver, ApplicationSender):
    _name = "Storage"
    _id = ObjectWithID._local_id_start

    def __init__(self, capacity):
        super(Storage, self).__init__()
        self.capacity = capacity
        self.application_quantity = 0
        self.applications = []

    def _get_application(self):
        self.application_quantity -= 1
        return self.applications.pop(0)

    def _append_application(self, value):
        self.application_quantity += 1
        self.applications.append(value)

    def can_receive_application(self):
        return self.application_quantity < self.capacity

    def receive_application(self, current_time, application):
        if not self.can_receive_application():
            raise Exception("{} is full".format(self._name))
        self._append_application(application)
        logging.info(
            "{} {} received application, total quantity: {} of {}".format(self._name, self.local_id,
                                                                          self.application_quantity,
                                                                          self.capacity))

    def is_empty(self):
        return self.application_quantity <= 0

    def take_application(self):
        if self.is_empty():
            raise Exception("{} is empty".format(self._name))
        logging.info("{} {} sent application, total quantity: {} of {}".format(self._name, self.local_id,
                                                                               self.application_quantity,
                                                                               self.capacity))
        return self._get_application()

    def clear(self):
        self.application_quantity = 0
        del self.applications[:]


class StorageWithStatistics(Storage):
    _id = ObjectWithID._local_id_start

    def __init__(self, capacity):
        super(StorageWithStatistics, self).__init__(capacity)
        self.statistics = {i: 0 for i in range(capacity + 1)}
        self.statistics[0] = 1

    def _get_application(self):
        application = super(StorageWithStatistics, self)._get_application()
        self.statistics[self.application_quantity] += 1
        return application

    def _append_application(self, value):
        super(StorageWithStatistics, self)._append_application(value)
        self.statistics[self.application_quantity] += 1

    def clear(self):
        super(StorageWithStatistics, self).clear()
        self.statistics = {i: 0 for i in self.statistics.keys()}
        self.statistics[0] = 1


class StorageWithRefuse(Storage):
    _name = "StorageWithRefuse"
    _id = ObjectWithID._local_id_start

    def __init__(self, capacity):
        super(StorageWithRefuse, self).__init__(capacity)
        self.refused_cache = []
        self.refused_applications = 0

    def can_receive_application(self):
        return True

    def receive_application(self, current_time, application):
        if not super(StorageWithRefuse, self).can_receive_application():
            self.refused_applications += 1
            self.refused_cache.append(application)
            logging.info(
                "{} {} lost application, total lost quantity: {}".format(self._name, self.local_id,
                                                                         self.refused_applications))
        else:
            self._append_application(application)
            logging.info(
                "{} {} received application, total quantity: {} of {}".format(self._name, self.local_id,
                                                                              self.application_quantity,
                                                                              self.capacity))

    def clear(self):
        super(StorageWithRefuse, self).clear()
        del self.refused_cache[:]
        self.refused_applications = 0


class StorageWithRefuseWithStatistics(StorageWithRefuse):
    _id = ObjectWithID._local_id_start

    def __init__(self, capacity):
        super(StorageWithRefuseWithStatistics, self).__init__(capacity)
        self.statistics = {i: 0 for i in range(capacity + 1)}
        self.statistics[0] = 0

    def _get_application(self):
        application = super(StorageWithRefuseWithStatistics, self)._get_application()
        self.statistics[self.application_quantity] += 1
        return application

    def _append_application(self, value):
        super(StorageWithRefuseWithStatistics, self)._append_application(value)
        self.statistics[self.application_quantity] += 1

    def clear(self):
        super(StorageWithRefuseWithStatistics, self).clear()
        self.statistics = {i: 0 for i in self.statistics.keys()}
        self.statistics[0] = 0


class Phase(ObjectWithID, ApplicationReceiver):
    """
    :type storage:Storage
    :type channels:list[Channel]
    :type next_receiver:ApplicationReceiver
    """
    _name = "Phase"
    _id = ObjectWithID._local_id_start

    def __init__(self, storage, channel_distrib, distrib_params, channel_quatity, next_receiver=None,
                 enable_statistics=True):
        """
        :type distrib_params:DistributionParams
        """
        super(Phase, self).__init__()
        self.storage = storage
        self.channels = []
        if enable_statistics:
            for i in xrange(channel_quatity):
                self.channels.append(ChannelWithStatistics(channel_distrib,
                                                           DistributionParams(list(distrib_params.param_names),
                                                                              *distrib_params.defargs,
                                                                              **distrib_params.defkwargs)))
        else:
            for i in xrange(channel_quatity):
                self.channels.append(Channel(channel_distrib, DistributionParams(list(distrib_params.param_names),
                                                                                 *distrib_params.defargs,
                                                                                 **distrib_params.defkwargs)))
        self.next_receiver = next_receiver

    def can_receive_application(self):
        for chn in self.channels:
            if chn.is_free():
                return True
        return self.storage.can_receive_application()

    def receive_application(self, current_time, application):
        if not self.can_receive_application():
            raise Exception("Next phase can't receive application")
        for chn in self.channels:
            if chn.is_free():
                chn.start_service(current_time, application)
                break
        else:
            self.storage.receive_application(current_time, application)
        logging.info("{} {} received application".format(self._name, self.local_id))

    def process_channels(self, current_time):
        for chn in self.channels:
            if not chn.is_free():
                if chn.is_blocked() or (chn.is_busy() and chn.service_completed(current_time)):
                    if self.next_receiver.can_receive_application():
                        self.next_receiver.receive_application(current_time, chn.application)
                        chn.complete_service(current_time)
                    else:
                        logging.debug(
                            "{} {} can't receive application from channel {}".format(self._name,
                                                                                     self.next_receiver.local_id,
                                                                                     chn.local_id))
                        chn.set_blocked()

    def process_storage(self, current_time):
        for chn in self.channels:
            if self.storage.is_empty():
                break
            if chn.is_free():
                chn.start_service(current_time, self.storage.take_application())

    def process_phase(self, current_time):
        self.process_storage(current_time)
        self.process_channels(current_time)

    def clear(self):
        self.storage.clear()
        for chn in self.channels:
            chn.clear()


class Source(ObjectWithID):
    """
    :type start_phase:Phase
    """
    _name = "Source"
    _id = ObjectWithID._local_id_start

    def __init__(self, time_distrib, start_phase=None):
        super(Source, self).__init__()
        self.time_distrib = time_distrib
        self.next_application_time = 0
        self.start_phase = start_phase
        self.application_quantity = 0
        self.next_application = None

    def generate_applicaiton(self, current_time):
        self.next_application_time = current_time + self.time_distrib.rvs(size=1)[0]
        self.next_application = Application(self.next_application_time)
        self.application_quantity += 1
        logging.info(
            "Next application will be generated in {} {} at {}".format(self._name, self.local_id,
                                                                       self.next_application_time))

    def send_application(self, current_time):
        if self.next_application_time <= current_time:
            logging.info("{} sent application to the beginning".format(self._name))
            self.start_phase.receive_application(current_time, self.next_application)
            self.generate_applicaiton(current_time)

    def clear(self):
        self.next_application_time = 0
        self.application_quantity = 0
        self.next_application = None


class QSchemeSimulator(object):
    """
    :type source:Source
    :type phases: list[Phase]
    :type end_storage:EndStorage
    t_n:current time
    delta_t: simulation interval
    """

    def __init__(self, source, phases, end_storage):
        """
        :type phases:list[Phase]
        """
        self.source = source
        self.source.generate_applicaiton(0)
        self.phases = phases
        self.end_storage = end_storage
        self.t_n = 0
        self.delta_t = 0.01
        source.start_phase = phases[0]
        for i in xrange(len(phases) - 1):
            phases[i].next_receiver = phases[i + 1]
        phases[-1].next_receiver = end_storage

    def _continue_loop(self):
        return self.end_storage.application_quantity < 1000

    def loop(self):
        for phase in reversed(self.phases):
            phase.process_phase(self.t_n)
        self.source.send_application(self.t_n)
        self.t_n += self.delta_t

    def clear(self):
        self.source.clear()
        self.end_storage.clear()
        for phase in self.phases:
            phase.clear()
        self.source.generate_applicaiton(0)
        self.t_n = 0
