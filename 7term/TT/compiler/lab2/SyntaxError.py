class SyntaxError(Exception):
    def __init__(self, production, expected, found):
        self.expected = expected
        self.found = found
        self.production = production

    def __str__(self):
        return "In {0} expected {1}, found {2}".format(self.production, self.expected, self.found)
