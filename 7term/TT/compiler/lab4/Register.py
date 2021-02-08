class Register(object):
    def __init__(self):
        self.register = RegisterGenerator.get_next()
        self.value = 0

    def __str__(self):
        return self.register


class RegisterGenerator(object):
    _next_register = 0

    @classmethod
    def get_next(cls):
        next_register = cls._next_register
        cls._next_register += 1
        return "R{0}".format(next_register)
