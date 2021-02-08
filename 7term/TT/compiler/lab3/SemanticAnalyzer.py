from ..lab2.TreeNode import TreeNode
from ..lab1.Type import Type
from ..lab1.Token import Token
from ..lab1.Tag import Tag
from ..lab2.NodeType import NodeType
from TypeException import TypeException
from SemanticException import SemanticException


class SemanticAnalyzer(object):
    def __init__(self, symbol_table, syntax_tree):
        """
        :type symbol_table:dict
        :type syntax_tree:TreeNode
        """
        self.symbol_table = symbol_table
        self.syntax_tree = syntax_tree

    def check_types(self):
        for block in self.syntax_tree.children:
            if block.node_type == NodeType.CONST_DEF:
                self.check_constant_definition(block)
            elif block.node_type == NodeType.VAR_DECL:
                self.check_variable_declaration(block)
            elif block.node_type == NodeType.SEQUENCE:
                self.check_sequence_type(block)

    def check_constant_definition(self, constant_definition):
        """
        :type constant_definition:TreeNode
        :type variable_declarations:TreeNode
        """
        for assingment in constant_definition.children:
            constant_token = assingment.children[0]
            number_token = assingment.children[1]
            if self.symbol_table[constant_token.attribute].declared:
                raise SemanticException("Double declaration", constant_token)
            else:
                self.symbol_table[constant_token.attribute].declared = True
                self.symbol_table[constant_token.attribute].constant = True
                self.symbol_table[constant_token.attribute].type = self.symbol_table[number_token.attribute].type

    def check_variable_declaration(self, variable_declaration):
        for colon_block in variable_declaration.children:
            identifier_list = colon_block.children[0]
            type_token = colon_block.children[1]
            for identifier_token in identifier_list.children:
                if self.symbol_table[identifier_token.attribute].declared:
                    raise SemanticException("Double declaration", identifier_token)
                else:
                    self.symbol_table[identifier_token.attribute].declared = True
                    self.symbol_table[identifier_token.attribute].constant = False
                    self.symbol_table[identifier_token.attribute].type = Type.get_type_by_token(type_token)

    def check_sequence_type(self, sequence_block):
        """
        :type sequence_block:TreeNode
        """
        for statement in sequence_block.children:
            self.check_statement_type(statement)

    def check_statement_type(self, statement_block):
        """
        :type statement_block:TreeNode
        """
        if statement_block.node_type == NodeType.ASSIGNMENT:
            identifier_token = statement_block.children[0]
            if self.symbol_table[identifier_token.attribute].constant:
                raise SemanticException("Cant assign to constant", identifier_token)
            if not self.symbol_table[identifier_token.attribute].declared:
                raise SemanticException("Variable not declared", identifier_token)
            identifier_type = self.symbol_table[identifier_token.attribute].type
            expression_type = self.get_expression_type(statement_block.children[1])
            if identifier_type in (Type.BOOLEAN, Type.INTEGER) and identifier_type != expression_type:
                raise TypeException(statement_block, expression_type, identifier_type)
            if identifier_type==Type.REAL and expression_type==Type.BOOLEAN:
                raise TypeException(statement_block, expression_type, Type.REAL, Type.INTEGER)
        elif statement_block.node_type == NodeType.IF:
            expression = statement_block.children[0]
            expression_type = self.get_expression_type(expression)
            if expression_type != Type.BOOLEAN:
                raise TypeException(statement_block, expression_type, Type.BOOLEAN)
            then_statement = statement_block.children[1]
            self.check_statement_type(then_statement)
            if len(statement_block.children) > 2:
                else_statement = statement_block.children[2]
                self.check_statement_type(else_statement)
        elif statement_block.node_type == NodeType.WHILE:
            expression = statement_block.children[0]
            statement = statement_block.children[1]
            expression_type = self.get_expression_type(expression)
            if expression_type != Type.BOOLEAN:
                raise TypeException(statement_block, expression_type, Type.BOOLEAN)
            self.check_statement_type(statement)
        elif statement_block.node_type == NodeType.COMPOSED:
            sequence = statement_block.children[0]
            self.check_sequence_type(sequence)

    def get_expression_type(self, expression):
        if isinstance(expression, TreeNode):
            if expression.node_type in (
                    NodeType.RELATION_EQUAl, NodeType.RELATION_NON_EQUAL, NodeType.RELATION_LESS,
                    NodeType.RELATION_LESS_EQUAL,
                    NodeType.RELATION_GREATER, NodeType.RELATION_GREATER_EQUAL):
                first_operand_type = self.get_expression_type(expression.children[0])
                second_operand_type = self.get_expression_type(expression.children[1])
                if (first_operand_type in (Type.INTEGER, Type.REAL) and second_operand_type == Type.BOOLEAN) or (
                                first_operand_type == Type.BOOLEAN and second_operand_type in (
                        Type.REAL, Type.INTEGER)):
                    raise TypeException(expression, Type.BOOLEAN, Type.REAL, Type.INTEGER)
                return Type.BOOLEAN
            elif expression.node_type in (NodeType.OPERATOR_UNARY_MINUS, NodeType.OPERATOR_UNARY_PLUS):
                first_operand_type = self.get_expression_type(expression.children[0])
                if first_operand_type not in (Type.REAL, Type.INTEGER):
                    raise TypeException(expression, first_operand_type, Type.REAL, Type.INTEGER)
                return first_operand_type
            elif expression.node_type in (
                    NodeType.OPERATOR_PLUS, NodeType.OPERATOR_MINUS, NodeType.OPERATOR_MULTIPLY,
                    NodeType.OPERATOR_DIVISION):
                first_operand_type = self.get_expression_type(expression.children[0])
                second_operand_type = self.get_expression_type(expression.children[1])
                if first_operand_type not in (Type.REAL, Type.INTEGER):
                    raise TypeException(expression, first_operand_type, Type.REAL, Type.INTEGER)
                if second_operand_type not in (Type.REAL, Type.INTEGER):
                    raise TypeException(expression, second_operand_type, Type.REAL, Type.INTEGER)
                if first_operand_type == Type.REAL or second_operand_type == Type.REAL:
                    return Type.REAL
                else:
                    return Type.INTEGER
            elif expression.node_type == NodeType.OPERATOR_NOT:
                first_operand_type = self.get_expression_type(expression.children[0])
                if first_operand_type != Type.BOOLEAN:
                    raise TypeException(expression, first_operand_type, Type.BOOLEAN)
                return Type.BOOLEAN
            elif expression.node_type in (NodeType.OPERATOR_AND, NodeType.OPERATOR_OR):
                first_operand_type = self.get_expression_type(expression.children[0])
                second_operand_type = self.get_expression_type(expression.children[1])
                if first_operand_type != Type.BOOLEAN:
                    raise TypeException(expression, first_operand_type, Type.BOOLEAN)
                if second_operand_type != Type.BOOLEAN:
                    raise TypeException(expression, second_operand_type, Type.BOOLEAN)
                return Type.BOOLEAN
            elif expression.node_type in (NodeType.OPERATOR_MOD, NodeType.OPERATOR_DIV):
                first_operand_type = self.get_expression_type(expression.children[0])
                second_operand_type = self.get_expression_type(expression.children[1])
                if first_operand_type != Type.INTEGER:
                    raise TypeException(expression, first_operand_type, Type.INTEGER)
                if second_operand_type != Type.INTEGER:
                    raise TypeException(expression, first_operand_type, Type.INTEGER)
                return Type.INTEGER
        elif isinstance(expression, Token):
            if expression.tag == Tag.ID:
                if not self.symbol_table[expression.attribute].declared:
                    raise SemanticException("Variable not declared", expression)
                else:
                    return self.symbol_table[expression.attribute].type
            elif expression.tag == Tag.NUM:
                return self.symbol_table[expression.attribute].type
            elif expression.tag in (Tag.TRUE, Tag.FALSE):
                return Type.BOOLEAN
