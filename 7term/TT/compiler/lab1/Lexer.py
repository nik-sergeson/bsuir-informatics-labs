from Tag import Tag
import re
from Token import Token
from LexerException import LexerException
from Identifier import Identifier
from Number import Number
from Type import Type


class Lexer(object):
    input_buffer = None
    symbol_table = {}
    number_re = "^[0-9]+(\.[0-9]+)?(E[+-]?[0-9]+)?$"
    number_re_next_symbol = "^[0-9]+(\.[0-9]*)?(E[+-]?[0-9]*)?$"

    RESERVED_WORDS = {"program": Token(Tag.PROGRAM), "var": Token(Tag.VAR), "real": Token(Tag.REAL),
                      "integer": Token(Tag.INTEGER), "if": Token(Tag.IF), "else": Token(Tag.ELSE),
                      "begin": Token(Tag.BEGIN), "end": Token(Tag.END), "writeln": Token(Tag.WRITELN),
                      "and": Token(Tag.LOGICAL_AND), "or": Token(Tag.LOGICAL_OR), "div": Token(Tag.DIV),
                      "mod": Token(Tag.MOD), "not": Token(Tag.LOGICAL_NOT), "then": Token(Tag.THEN),
                      "boolean": Token(Tag.BOOLEAN),
                      "shl": Token(Tag.SHL), "shr": Token(Tag.SHR), "True": Token(Tag.TRUE),
                      "False": Token(Tag.FALSE),
                      "xor": Token(Tag.LOGICAL_XOR), "const": Token(Tag.CONST)}

    LIMITERS = {'+': Token(Tag.PLUS), '-': Token(Tag.MINUS), '*': Token(Tag.ASTERISK), '/': Token(Tag.SLASH),
                '=': Token(Tag.EQUAL), '<': Token(Tag.LESS_THAN), '>': Token(Tag.GREATER_THAN),
                '[': Token(Tag.LEFT_BRACKET),
                ']': Token(Tag.RIGHT_BRACKET), '.': Token(Tag.PERIOD), ',': Token(Tag.COMMA),
                ':': Token(Tag.COLON),
                ';': Token(Tag.SEMICOLON), '(': Token(Tag.LEFT_PARANTHESIS), ')': Token(Tag.RIGHT_PARANTHESIS),
                '<>': Token(Tag.NON_EQUAL), '<=': Token(Tag.LESS_THAN_EQUAL), '>=': Token(Tag.GREATER_THAN_EQUAL),
                ':=': Token(Tag.ASSIGNMENT), '**': Token(Tag.POWER), '!=': Token(Tag.NOT_EQUAL)}

    def __init__(self, input_str):
        self.input_buffer = input_str

    def next_token(self):
        current_state = "start"
        current_buffer = ""
        while True:
            if current_state == "start":
                if not self.input_buffer:
                    return None
                elif self.input_buffer[0] in (' ', '\n', '\r', '\t'):
                    self.input_buffer = self.input_buffer[1:]
                elif self.input_buffer[0].isalpha():
                    current_buffer += self.input_buffer[0]
                    self.input_buffer = self.input_buffer[1:]
                    current_state = "identifier"
                elif self.input_buffer[0].isdigit():
                    current_buffer += self.input_buffer[0]
                    self.input_buffer = self.input_buffer[1:]
                    current_state = "number"
                elif self.input_buffer[0] in ('<', '>', ':', '*', '!'):
                    current_buffer += self.input_buffer[0]
                    self.input_buffer = self.input_buffer[1:]
                    current_state = "may-double-lmtr"
                elif self.input_buffer[0] in self.LIMITERS:
                    current_buffer += self.input_buffer[0]
                    self.input_buffer = self.input_buffer[1:]
                    current_state = "limiter"
                else:
                    raise LexerException("Unexpected symbol", self.input_buffer[0])
            elif current_state == "identifier":
                if self.input_buffer and (self.input_buffer[0].isalpha() or self.input_buffer[0].isdigit()):
                    current_buffer += self.input_buffer[0]
                    self.input_buffer = self.input_buffer[1:]
                else:
                    if current_buffer in self.RESERVED_WORDS:
                        return self.RESERVED_WORDS[current_buffer].copy()
                    else:
                        if current_buffer not in self.symbol_table:
                            self.symbol_table[current_buffer] = Identifier(current_buffer, None)
                        return Token(Tag.ID, current_buffer)
            elif current_state == "number":
                if self.input_buffer and re.search(self.number_re_next_symbol,
                                                   current_buffer + self.input_buffer[0]) is not None:
                    current_buffer += self.input_buffer[0]
                    self.input_buffer = self.input_buffer[1:]
                else:
                    if re.search(self.number_re, current_buffer) is None:
                        raise LexerException("Invalid number format", current_buffer)
                    if current_buffer not in self.symbol_table:
                        if '.' in current_buffer:
                            self.symbol_table[current_buffer] = Number(float(current_buffer), Type.REAL)
                        else:
                            self.symbol_table[current_buffer] = Number(int(current_buffer), Type.INTEGER)
                    return Token(Tag.NUM, current_buffer)
            elif current_state == "may-double-lmtr":
                if current_buffer[-1] == '<':
                    if self.input_buffer and self.input_buffer[0] in ('>', '='):
                        current_buffer += self.input_buffer[0]
                        self.input_buffer = self.input_buffer[1:]
                        return self.LIMITERS[current_buffer].copy()
                    else:
                        return self.LIMITERS[current_buffer].copy()
                if current_buffer[-1] == '>':
                    if self.input_buffer and self.input_buffer[0] == '=':
                        current_buffer += self.input_buffer[0]
                        self.input_buffer = self.input_buffer[1:]
                        return self.LIMITERS[current_buffer].copy()
                    else:
                        return self.LIMITERS[current_buffer].copy()
                if current_buffer[-1] == ':':
                    if self.input_buffer and self.input_buffer[0] == '=':
                        current_buffer += self.input_buffer[0]
                        self.input_buffer = self.input_buffer[1:]
                        return self.LIMITERS[current_buffer].copy()
                    else:
                        return self.LIMITERS[current_buffer].copy()
                if current_buffer[-1] == '*':
                    if self.input_buffer and self.input_buffer[0] == '*':
                        current_buffer += self.input_buffer[0]
                        self.input_buffer = self.input_buffer[1:]
                        return self.LIMITERS[current_buffer].copy()
                    else:
                        return self.LIMITERS[current_buffer].copy()
                if current_buffer[-1] == '!':
                    if self.input_buffer and self.input_buffer[0] == '=':
                        current_buffer += self.input_buffer[0]
                        self.input_buffer = self.input_buffer[1:]
                        return self.LIMITERS[current_buffer].copy()
                    else:
                        return self.LIMITERS[current_buffer].copy()
            elif current_state == "limiter":
                return self.LIMITERS[current_buffer].copy()
