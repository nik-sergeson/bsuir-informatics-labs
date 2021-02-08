from compiler.lab1.Lexer import Lexer
from compiler.lab2.Parser import Parser
from compiler.lab2.TreeVisualizer import TreeVisualizer

if __name__ == "__main__":
    pascal_prog = "program lab1; const tempcont=10; tempcost1=20;var cost, price, tax: real;begin cost:=(price+tax)*0.98;if(cost<10)then begin cost:=10; end else cost:=100; end."
    lexer = Lexer(pascal_prog)
    parser = Parser(lexer)
    syntax_tree = parser.parse()
    tree_visualizer = TreeVisualizer(syntax_tree)
    tree_visualizer.show_graph()
