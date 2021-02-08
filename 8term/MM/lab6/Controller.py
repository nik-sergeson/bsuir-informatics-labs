from __future__ import division
from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from QSchemeSimulator import *
from Statistics import *
import yaml


class Controller(QWidget):
    """
    :type progbar_mapping:dict[int, QProgressBar]
    :type edit_mapping:dict[int, QLineEdit]
    :type phase_distrib_params:dict[int, dict[str, QLineEdit]]
    :type qscheme:QSchemeSimulator
    """

    def __init__(self, qscheme, max_chn_quantity):
        """
        :type qscheme: QSchemeSimulator
        """
        QWidget.__init__(self)
        layout = QGridLayout(self)
        self.progbar_mapping = {}
        self.edit_mapping = {}
        self.phase_distrib_params = {}
        self.qscheme = qscheme
        self.storage_table = QTableWidget()
        self.storage_table.setRowCount(1)
        self.storage_table.setColumnCount(len(qscheme.phases))
        self.storage_table.setVerticalHeaderLabels(["Quantity"])
        self.storage_table.setHorizontalHeaderLabels(
            ["{} {}".format(phase.storage._name, phase.storage.local_id) for phase in qscheme.phases])
        self.channel_table = QTableWidget()
        chn_names = []
        for phase in qscheme.phases:
            for chn in phase.channels:
                chn_names.append("Channel {}".format(chn.local_id))
        self.channel_table.setRowCount(3)
        self.channel_table.setColumnCount(len(chn_names))
        self.channel_table.setHorizontalHeaderLabels(chn_names)
        self.channel_table.setVerticalHeaderLabels(["Free", "Busy", "Blocked"])
        col = 0
        for phase in qscheme.phases:
            if isinstance(phase.storage, StorageWithRefuse):
                self.progbar_mapping[phase.storage.id] = [QProgressBar(self), QProgressBar(self)]
                refuse_label = QLabel("Refused:", self)
                layout.addWidget(self.progbar_mapping[phase.storage.id][0], 4, col, 1, 2)
                layout.addWidget(self.progbar_mapping[phase.storage.id][1], 5, col + 1, 1, 1)
                layout.addWidget(refuse_label, 5, col, 1, 1)
            else:
                self.progbar_mapping[phase.storage.id] = QProgressBar(self)
                layout.addWidget(self.progbar_mapping[phase.storage.id], 4, col, 1, 2)
            storage_label = QLabel("Storage size:", self)
            self.edit_mapping[phase.storage.id] = QLineEdit(str(phase.storage.capacity), self)
            layout.addWidget(storage_label, 0, col, 1, 1)
            layout.addWidget(self.edit_mapping[phase.storage.id], 0, col + 1, 1, 1)
            col += 2
            row = (max_chn_quantity - len(phase.channels)) // 2 + 2
            self.phase_distrib_params[phase.id] = {}
            param_row = 0
            for param in phase.channels[0].distrib_params.param_names:
                param_label = QLabel(param, self)
                layout.addWidget(param_label, param_row, col, 1, 1)
                self.phase_distrib_params[phase.id][param] = QLineEdit(
                    str(phase.channels[0].distrib_params.defkwargs[param]), self)
                layout.addWidget(self.phase_distrib_params[phase.id][param], param_row, col + 1, 1, 1)
                param_row += 1
            for chn in phase.channels:
                self.progbar_mapping[chn.id] = QProgressBar(self)
                layout.addWidget(self.progbar_mapping[chn.id], row, col, 1, 2)
                row += 1
            col += 2
        self.progbar_mapping[qscheme.end_storage.id] = QProgressBar(self)
        layout.addWidget(self.progbar_mapping[qscheme.end_storage.id], 4, col, 1, 2)
        self.simulate_button = QPushButton('Simulate', self)
        self.simulate_button.clicked.connect(self.simulate_button_clicked)
        self.cancelled = False
        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)
        layout.addWidget(self.simulate_button, 0, col, 1, 1)
        layout.addWidget(self.cancel_button, 1, col, 1, 1)
        self.spacing_hist = MyMplCanvas(self)
        self.duraction_hist = MyMplCanvas(self)
        layout.addWidget(self.spacing_hist, 7, 0, 2, 11)
        layout.addWidget(self.duraction_hist, 7, 11, 2, 11)
        layout.addWidget(self.channel_table, 11, 0, 2, 22)
        layout.addWidget(self.storage_table, 9, 0, 1, 22)
        self.storage_table.setMaximumHeight(60)

    def simulate_button_clicked(self):
        for phase in self.qscheme.phases:
            phase.storage.capacity = int(self.edit_mapping[phase.storage.id].text())
            distrib_kwargs = {}
            for param, edit in self.phase_distrib_params[phase.id].items():
                distrib_kwargs[param] = yaml.load(str(edit.text()))
            for chn in phase.channels:
                chn.set_distrib_params(distrib_kwargs)
        while self.qscheme._continue_loop() and not self.cancelled:
            self.qscheme.loop()
            self.update_progress_bars()
            QApplication.processEvents()
        if self.cancelled:
            self.qscheme.clear()
            self.cancelled = False
        else:
            self.draw_bars()
            self.fill_table()

    def cancel_button_clicked(self):
        self.cancelled = True

    def update_progress_bars(self):
        for phase in self.qscheme.phases:
            if isinstance(phase.storage, StorageWithRefuse):
                self.progbar_mapping[phase.storage.id][0].setValue(
                    100 * phase.storage.application_quantity / phase.storage.capacity)
                self.progbar_mapping[phase.storage.id][1].setValue(
                    round(100 * phase.storage.refused_applications / self.qscheme.source.application_quantity))
            else:
                self.progbar_mapping[phase.storage.id].setValue(
                    100 * phase.storage.application_quantity / phase.storage.capacity)
            for chn in phase.channels:
                if chn.is_free():
                    self.progbar_mapping[chn.id].setValue(0)
                else:
                    self.progbar_mapping[chn.id].setValue(100)
        self.progbar_mapping[self.qscheme.end_storage.id].setValue(
            round(100 * self.qscheme.end_storage.application_quantity / self.qscheme.source.application_quantity))

    def draw_bars(self):
        statist = EndStorageStatistics(self.qscheme.end_storage)
        self.spacing_hist.compute_figure(statist.get_application_spacing(), "Application spacing", bins=20)
        self.duraction_hist.compute_figure(statist.get_service_duraction(), "Service duraction", bins=50)

    def fill_table(self):
        for i, phase in enumerate(self.qscheme.phases):
            stats = phase.storage.statistics
            exp_value = estimate_expvalue(stats)
            if self.storage_table.item(0, i) is not None:
                self.storage_table.item(0, i).setText(str(round(exp_value, 2)))
            else:
                self.storage_table.setItem(0, i, QTableWidgetItem(str(round(exp_value, 2))))
            for chn in phase.channels:
                cond_stats = chn.get_probabilities()
                for cond, val in cond_stats.items():
                    if self.channel_table.item(cond, chn.local_id - 1) is not None:
                        self.channel_table.item(cond, chn.local_id - 1).setText(str(round(val, 2)))
                    else:
                        self.channel_table.setItem(cond, chn.local_id - 1, QTableWidgetItem(str(round(val, 2))))


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_figure(self, values, title, bins=10):
        self.axes.hist(values, normed=True, bins=bins)
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Density')
        exp_value = estimate_expvalue(values)
        dispersion = estimate_dispersion(values)
        self.axes.set_title(title + " M={:.2f} D={:.2f}".format(exp_value, dispersion))
        self.draw()
