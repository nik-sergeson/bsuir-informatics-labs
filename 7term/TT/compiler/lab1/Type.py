from Tag import Tag
from Token import Token


class Type(object):
    BOOLEAN, INTEGER, REAL = range(3)
    _type_str = ["boolean", "integer", "real"]

    @staticmethod
    def get_type_by_token(token):
        """
        :type token: Token
        """
        if token.tag == Tag.BOOLEAN:
            return Type.BOOLEAN
        elif token.tag == Tag.INTEGER:
            return Type.INTEGER
        elif token.tag == Tag.REAL:
            return Type.REAL
        else:
            return None

    @classmethod
    def get_type_name(cls, type):
        return cls._type_str[type]
