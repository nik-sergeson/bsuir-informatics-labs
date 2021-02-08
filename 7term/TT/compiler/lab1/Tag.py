class Tag(object):
    NUM, ID, IF, ELSE, WHILE, PROGRAM, VAR, REAL, INTEGER, BEGIN, END, WRITELN, LOGICAL_AND, LOGICAL_OR, DIV, MOD, \
    THEN, CHAR, BOOLEAN, SHL, SHR, TRUE, FALSE, LOGICAL_XOR, PLUS, MINUS, ASTERISK, SLASH, EQUAL, LOGICAL_NOT, \
    LESS_THAN, GREATER_THAN, LEFT_BRACKET, RIGHT_BRACKET, PERIOD, COMMA, COLON, SEMICOLON, LEFT_PARANTHESIS, \
    RIGHT_PARANTHESIS, NON_EQUAL, LESS_THAN_EQUAL, GREATER_THAN_EQUAL, ASSIGNMENT, POWER, NOT_EQUAL, CONST = range(47)

    tag_names = ["NUM", "ID", "IF", "ELSE", "WHILE", "PROGRAM", "VAR", "REAL", "INTEGER", "BEGIN", "END", "WRITELN",
                   "LOGICAL_AND", "LOGICAL_OR", "DIV", "MOD", "THEN", "CHAR", "BOOLEAN", "SHL", "SHR", "TRUE", "FALSE",
                   "LOGICAL_XOR", "PLUS", "MINUS", "ASTERISK", "SLASH", "EQUAL", "LOGICAL_NOT", "LESS_THAN",
                   "GREATER_THAN",
                   "LEFT_BRACKET", "RIGHT_BRACKET", "PERIOD", "COMMA", "COLON", "SEMI_COLON", "LEFT_PARANTHESIS",
                   "RIGHT_PARANTHESIS", "NON_EQUAL", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", "ASSIGNMENT", "POWER", "NOT_EQUAL", "CONST"]

    @classmethod
    def get_token_tag_name(cls, token):
        return cls.tag_names[token.tag]

    @classmethod
    def get_name(cls, tag):
        return cls.tag_names[tag]
