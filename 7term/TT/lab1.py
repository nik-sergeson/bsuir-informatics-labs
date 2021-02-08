from __future__ import print_function

from compiler.lab1.Tag import Tag
from compiler.lab1.Lexer import Lexer

if __name__ == "__main__":
    pascal_prog = "program lab1; var cost, price, tax: real;begin cost:=(price+tax)*0.98;if(cost<10)then cost:=10;else cost:=100; end."
    lexer = Lexer(pascal_prog)
    next_tok = lexer.next_token()
    while next_tok is not None:
        print("({0}, {1})".format(Tag.get_token_tag_name(next_tok), next_tok.attribute))
        next_tok = lexer.next_token()
    print("Symbol table:")
    for symb in lexer.symbol_table:
        print("{0}: {1}".format(symb, type(lexer.symbol_table[symb])))
