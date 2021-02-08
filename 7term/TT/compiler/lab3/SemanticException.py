class SemanticException(Exception):
    def __init__(self, message, token=None):
        if token is None:
            super(SemanticException, self).__init__(message)
        else:
            super(SemanticException, self).__init__(message + ': ' + token.__str__())