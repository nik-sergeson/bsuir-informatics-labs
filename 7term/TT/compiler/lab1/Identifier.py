class Identifier(object):
    def __init__(self, name, value, declared=False, id_type=None, constant=False):
        self.name = name
        self.value = value
        self.declared = declared
        self.type = id_type
        self.constant = constant

    def __str__(self):
        return self.name