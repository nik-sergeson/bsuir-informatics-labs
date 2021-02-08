class LexerException(Exception):
    def __init__(self, message, lexeme):
        super(LexerException, self).__init__(message + ' ' + lexeme)
