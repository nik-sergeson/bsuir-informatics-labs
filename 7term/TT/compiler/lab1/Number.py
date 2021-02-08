class Number(object):
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        return self.value.__str__()