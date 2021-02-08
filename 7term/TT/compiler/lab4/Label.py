class Label(object):
    def __init__(self):
        self.label = LabelGenerator.get_next()

    def __str__(self):
        return self.label

    def __eq__(self, other):
        return self.label == other.label


class LabelGenerator(object):
    _next_label = 0

    @classmethod
    def get_next(cls):
        next_label = cls._next_label
        cls._next_label += 1
        return "label{0}".format(next_label)
