from compiler.lab1.Lexer import Lexer
from compiler.lab2.Parser import Parser
from compiler.lab3.SemanticAnalyzer import SemanticAnalyzer
from compiler.lab4.Translator import Translator
from compiler.lab4.VirtualMachine import VirtualMachine

if __name__ == "__main__":
    pascal_prog = "program lab1; const tempcont=10; tempcost1=20;var cost, price, tax: real;begin price:=(price+tax)*0.98;if(cost<10)then cost:=10 else cost:=100; end."
    lexer = Lexer(pascal_prog)
    parser = Parser(lexer)
    syntax_tree = parser.parse()
    analyzer=SemanticAnalyzer(lexer.symbol_table, syntax_tree)
    analyzer.check_types()
    translator=Translator(syntax_tree, lexer.symbol_table)
    instructions=translator.generate_internal_state()
    for instruction in instructions:
        print(instruction)
    vm=VirtualMachine()
    vm.execute(instructions, lexer.symbol_table)
    print("cost:={0}".format(lexer.symbol_table["cost"].value))