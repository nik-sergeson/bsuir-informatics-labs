from compiler.lab1.Lexer import Lexer
from compiler.lab2.Parser import Parser
from compiler.lab3.SemanticAnalyzer import SemanticAnalyzer

if __name__ == "__main__":
    pascal_prog = "program lab1; const tempcont=10; tempcost1=20;var cost, price, tax: real;begin tempcont:=(price+tax)*0.98;if(cost<10)then cost:=10 else cost:=100; end."
    lexer = Lexer(pascal_prog)
    parser = Parser(lexer)
    syntax_tree = parser.parse()
    analyzer=SemanticAnalyzer(lexer.symbol_table, syntax_tree)
    analyzer.check_types()

