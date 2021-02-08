from ..lab1.Tag import Tag

from SyntaxError import SyntaxError
from NodeType import NodeType
from TreeNode import TreeNode


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.next_token()

    def get_next_token(self):
        self.current_token = self.lexer.next_token()

    def parse(self):
        program_node = TreeNode(NodeType.PROGRAM, self.parse_heading(), *self.parse_block().children)
        if self.current_token.tag != Tag.PERIOD:
            raise SyntaxError("statements", Tag.get_name(Tag.PERIOD), Tag.get_token_tag_name(self.current_token))
        else:
            self.get_next_token()
        return program_node

    def parse_heading(self):
        heading_node = TreeNode(NodeType.HEADING)
        if self.current_token.tag == Tag.PROGRAM:
            self.get_next_token()
        else:
            raise SyntaxError("heading", Tag.get_name(Tag.PROGRAM), Tag.get_token_tag_name(self.current_token))
        if self.current_token.tag == Tag.ID:
            heading_node.append_children(self.current_token)
            self.get_next_token()
        else:
            raise SyntaxError("heading", Tag.get_name(Tag.ID), Tag.get_token_tag_name(self.current_token))
        if self.current_token.tag == Tag.SEMICOLON:
            self.get_next_token()
        else:
            raise SyntaxError("heading", Tag.get_name(Tag.SEMICOLON), Tag.get_token_tag_name(self.current_token))
        return heading_node

    def parse_block(self):
        block_nodes = self.parse_declaration().children
        block_nodes.append(self.parse_statement_part())
        block_node = TreeNode(NodeType.STATEMENT, *block_nodes)
        return block_node

    def parse_declaration(self):
        declaration_node = TreeNode(NodeType.STATEMENT)
        constant_definition = self.parse_constant_definition_part()
        if constant_definition:
            declaration_node.append_children(constant_definition)
        variable_declaration = self.parse_variable_declaration_part()
        if variable_declaration:
            declaration_node.append_children(variable_declaration)
        return declaration_node

    def parse_constant_definition_part(self):
        constant_def = TreeNode(NodeType.CONST_DEF)
        if self.current_token.tag == Tag.CONST:
            self.get_next_token()
            constants = []
            while True:
                constant_node = self.parse_constant_definition()
                if constant_node:
                    constants.append(constant_node)
                else:
                    break
            if constants:
                constant_def.append_children(*constants)
                return constant_def
            else:
                raise SyntaxError("constant definition", "definitons", "none")
        else:
            return None

    def parse_constant_definition(self):
        constant_node = TreeNode(NodeType.CONST_ASSIGNMENT)
        if self.current_token.tag == Tag.ID:
            constant_node.append_children(self.current_token)
            self.get_next_token()
            if self.current_token.tag == Tag.EQUAL:
                self.get_next_token()
            else:
                raise SyntaxError("constant definition", Tag.get_name(Tag.EQUAL),
                                  Tag.get_token_tag_name(self.current_token))
            if self.current_token.tag == Tag.NUM:
                constant_node.append_children(self.current_token)
                self.get_next_token()
            else:
                raise SyntaxError("constant definition", Tag.get_name(Tag.NUM),
                                  Tag.get_token_tag_name(self.current_token))
            if self.current_token.tag == Tag.SEMICOLON:
                self.get_next_token()
            else:
                raise SyntaxError("constant definition", Tag.get_name(Tag.SEMICOLON),
                                  Tag.get_token_tag_name(self.current_token))
            return constant_node
        else:
            return None

    def parse_variable_declaration_part(self):
        var_decl = TreeNode(NodeType.VAR_DECL)
        if self.current_token.tag == Tag.VAR:
            self.get_next_token()
            variables = []
            while True:
                variable_node = self.parse_variable_declaration()
                if variable_node:
                    variables.append(variable_node)
                else:
                    break
            if variables:
                var_decl.append_children(*variables)
                return var_decl
            else:
                raise SyntaxError("variable declaration", "definitons", "none")
        else:
            return None

    def parse_variable_declaration(self):
        variable_node = TreeNode(NodeType.COLON)
        identifier_list = self.parse_identifier_list()
        if identifier_list:
            variable_node.append_children(identifier_list)
            if self.current_token.tag == Tag.COLON:
                self.get_next_token()
            else:
                raise SyntaxError("variable declaration", Tag.get_name(Tag.COLON),
                                  Tag.get_token_tag_name(self.current_token))
            if self.current_token.tag in (Tag.REAL, Tag.INTEGER, Tag.BOOLEAN):
                variable_node.append_children(self.current_token)
                self.get_next_token()
            else:
                raise SyntaxError("variable declaration", "Type", Tag.get_token_tag_name(self.current_token))
            if self.current_token.tag == Tag.SEMICOLON:
                self.get_next_token()
            else:
                raise SyntaxError("variable declaration", Tag.get_name(Tag.SEMICOLON),
                                  Tag.get_token_tag_name(self.current_token))
            return variable_node
        else:
            return None

    def parse_identifier_list(self):
        identifier_list_node = TreeNode(NodeType.IDENTIFIER_LIST)
        if self.current_token.tag == Tag.ID:
            identifier_list_node.append_children(self.current_token)
            self.get_next_token()
            while self.current_token.tag == Tag.COMMA:
                self.get_next_token()
                if self.current_token.tag == Tag.ID:
                    identifier_list_node.append_children(self.current_token)
                    self.get_next_token()
                else:
                    raise SyntaxError("variable definition", Tag.get_name(Tag.ID),
                                      self.current_token)
            return identifier_list_node
        else:
            return None

    def parse_statement_part(self):
        sequence_node = TreeNode(NodeType.SEQUENCE)
        if self.current_token.tag != Tag.BEGIN:
            raise SyntaxError("statements", Tag.get_name(Tag.BEGIN), self.current_token)
        else:
            self.get_next_token()
        sequence_node.append_children(*self.parse_sequence().children)
        if self.current_token.tag != Tag.END:
            raise SyntaxError("statements", Tag.get_name(Tag.END), self.current_token)
        else:
            self.get_next_token()
        return sequence_node

    def parse_sequence(self):
        sequence_node = TreeNode(NodeType.STATEMENT)
        statement = self.parse_statement()
        if statement:
            if self.current_token.tag != Tag.SEMICOLON:
                raise SyntaxError("statement", Tag.get_name(Tag.SEMICOLON),
                                  self.current_token)
            else:
                self.get_next_token()
            sequence_node.append_children(statement)
            while True:
                statement = self.parse_statement()
                if statement:
                    if self.current_token.tag != Tag.SEMICOLON:
                        raise SyntaxError("statement", Tag.get_name(Tag.SEMICOLON),
                                          self.current_token)
                    else:
                        self.get_next_token()
                    sequence_node.append_children(statement)
                else:
                    break
            return sequence_node
        else:
            raise SyntaxError("statements", "statement", self.current_token)

    def parse_statement(self):
        if self.current_token.tag == Tag.ID:
            identifier = self.current_token
            self.get_next_token()
            if self.current_token.tag != Tag.ASSIGNMENT:
                raise SyntaxError("assignment", Tag.get_name(Tag.ASSIGNMENT),
                                  self.current_token)
            else:
                self.get_next_token()
            assignment_node = TreeNode(NodeType.ASSIGNMENT)
            assignment_node.append_children(identifier)
            assignment_node.append_children(self.parse_expression())
            return assignment_node
        elif self.current_token.tag == Tag.IF:
            self.get_next_token()
            expression = self.parse_expression()
            if self.current_token.tag == Tag.THEN:
                self.get_next_token()
                statement = self.parse_statement()
                if_node = TreeNode(NodeType.IF, expression, statement)
                if self.current_token.tag == Tag.ELSE:
                    self.get_next_token()
                    else_statement = self.parse_statement()
                    if_node.append_children(else_statement)
            else:
                raise SyntaxError("if statement", "THEN", self.current_token)
            return if_node
        elif self.current_token.tag == Tag.WHILE:
            self.get_next_token()
            expression = self.parse_expression()
            if self.current_token.tag == Tag.DO:
                self.get_next_token()
                statement = self.parse_statement()
                while_node = TreeNode(NodeType.WHILE, expression, statement)
            else:
                raise SyntaxError("while statement", "DO", self.current_token)
            return while_node
        elif self.current_token.tag == Tag.BEGIN:
            self.get_next_token()
            sequence = self.parse_sequence()
            if self.current_token.tag == Tag.END:
                self.get_next_token()
                composed_node = TreeNode(NodeType.COMPOSED, *sequence.children)
                return composed_node
            else:
                raise SyntaxError("composed statement", "END", self.current_token)
        else:
            return None

    def parse_expression(self):
        simple_expression = self.parse_simple_expression()
        if self.current_token.tag == Tag.EQUAL:
            self.get_next_token()
            expression_node = TreeNode(NodeType.RELATION_EQUAl)
            second_op = self.parse_simple_expression()
            expression_node.append_children(simple_expression, second_op)
            return expression_node
        elif self.current_token.tag == Tag.NON_EQUAL:
            self.get_next_token()
            expression_node = TreeNode(NodeType.RELATION_NON_EQUAL)
            second_op = self.parse_simple_expression()
            expression_node.append_children(simple_expression, second_op)
            return expression_node
        elif self.current_token.tag == Tag.LESS_THAN:
            self.get_next_token()
            expression_node = TreeNode(NodeType.RELATION_LESS)
            second_op = self.parse_simple_expression()
            expression_node.append_children(simple_expression, second_op)
            return expression_node
        elif self.current_token.tag == Tag.LESS_THAN_EQUAL:
            self.get_next_token()
            expression_node = TreeNode(NodeType.RELATION_LESS_EQUAL)
            second_op = self.parse_simple_expression()
            expression_node.append_children(simple_expression, second_op)
            return expression_node
        elif self.current_token.tag == Tag.GREATER_THAN:
            self.get_next_token()
            expression_node = TreeNode(NodeType.RELATION_GREATER)
            second_op = self.parse_simple_expression()
            expression_node.append_children(simple_expression, second_op)
            return expression_node
        elif self.current_token.tag == Tag.GREATER_THAN_EQUAL:
            self.get_next_token()
            expression_node = TreeNode(NodeType.RELATION_GREATER_EQUAL)
            second_op = self.parse_simple_expression()
            expression_node.append_children(simple_expression, second_op)
            return expression_node
        else:
            return simple_expression

    def parse_simple_expression(self):
        if self.current_token.tag == Tag.PLUS:
            term = self.parse_term()
            self.get_next_token()
            first_operand = TreeNode(NodeType.OPERATOR_UNARY_PLUS, term)
        elif self.current_token.tag == Tag.MINUS:
            term = self.parse_term()
            self.get_next_token()
            first_operand = TreeNode(NodeType.OPERATOR_UNARY_MINUS, term)
        else:
            first_operand = self.parse_term()
        if self.current_token.tag == Tag.PLUS:
            self.get_next_token()
            simple_expression_node = TreeNode(NodeType.OPERATOR_PLUS, first_operand, self.parse_term())
            return simple_expression_node
        elif self.current_token.tag == Tag.MINUS:
            self.get_next_token()
            simple_expression_node = TreeNode(NodeType.OPERATOR_MINUS, first_operand, self.parse_term())
            return simple_expression_node
        elif self.current_token.tag == Tag.LOGICAL_OR:
            self.get_next_token()
            simple_expression_node = TreeNode(NodeType.OPERATOR_OR, first_operand, self.parse_term())
            return simple_expression_node
        else:
            return first_operand

    def parse_term(self):
        first_operand = self.parse_factor()
        if self.current_token.tag == Tag.SLASH:
            self.get_next_token()
            second_operand = self.parse_factor()
            return TreeNode(NodeType.OPERATOR_DIVISION, first_operand, second_operand)
        elif self.current_token.tag == Tag.ASTERISK:
            self.get_next_token()
            second_operand = self.parse_factor()
            return TreeNode(NodeType.OPERATOR_MULTIPLY, first_operand, second_operand)
        elif self.current_token.tag == Tag.DIV:
            self.get_next_token()
            second_operand = self.parse_factor()
            return TreeNode(NodeType.OPERATOR_DIV, first_operand, second_operand)
        elif self.current_token.tag == Tag.MOD:
            self.get_next_token()
            second_operand = self.parse_factor()
            return TreeNode(NodeType.OPERATOR_MOD, first_operand, second_operand)
        elif self.current_token.tag == Tag.LOGICAL_AND:
            self.get_next_token()
            second_operand = self.parse_factor()
            return TreeNode(NodeType.OPERATOR_AND, first_operand, second_operand)
        else:
            return first_operand

    def parse_factor(self):
        if self.current_token.tag == Tag.ID:
            curr_token = self.current_token
            self.get_next_token()
            return curr_token
        elif self.current_token.tag == Tag.NUM:
            curr_token = self.current_token
            self.get_next_token()
            return curr_token
        elif self.current_token.tag == Tag.TRUE:
            curr_token = self.current_token
            self.get_next_token()
            return curr_token
        elif self.current_token.tag == Tag.FALSE:
            curr_token = self.current_token
            self.get_next_token()
            return curr_token
        elif self.current_token.tag == Tag.LEFT_PARANTHESIS:
            self.get_next_token()
            expression = self.parse_expression()
            if self.current_token.tag == Tag.RIGHT_PARANTHESIS:
                self.get_next_token()
            else:
                raise SyntaxError("expression with parenthesis", Tag.get_name(Tag.RIGHT_PARANTHESIS),
                                  self.current_token)
            return expression
        elif self.current_token.tag == Tag.LOGICAL_NOT:
            self.get_next_token()
            factor = self.parse_factor()
            return TreeNode(NodeType.OPERATOR_NOT, factor)
        else:
            raise SyntaxError("variable/number", "variable/number", self.current_token)
