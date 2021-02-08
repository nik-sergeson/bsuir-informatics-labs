from ..lab2.TreeNode import TreeNode
from ..lab2.NodeType import NodeType
from  TwoOperandInstruction import TwoOperandInstruction
from OperatorType import OperatorType
from Label import Label
from Register import Register
from ThreeOperandInstruction import ThreeOperandInstruction


class Translator(object):
    """
    :type symbol_table:dict
    :type syntax_tree:TreeNode
    """

    def __init__(self, syntax_tree, symbol_table):
        self.syntax_tree = syntax_tree
        self.symbol_table = symbol_table

    def generate_internal_state(self):
        for node in self.syntax_tree.children:
            if node.node_type == NodeType.SEQUENCE:
                return self.get_sequence_instructions(node)

    def get_sequence_instructions(self, current_node):
        """
        :type current_node:TreeNode
        :rtype list[tuple]
        """
        instruction_list = []
        if current_node.node_type in (NodeType.SEQUENCE, NodeType.COMPOSED):
            for statement in current_node.children:
                statement_instructions = self.get_statement_instructions(statement)
                instruction_list.extend(statement_instructions)
        return instruction_list

    def get_statement_instructions(self, current_node):
        """
        :type current_node:TreeNode
        :rtype list[TwoOperandInstruction]
        """
        instruction_list = []
        if current_node.node_type == NodeType.ASSIGNMENT:
            identifier = current_node.children[0]
            result, expression_instructions = self.get_expression_instructions(current_node.children[1])
            if expression_instructions:
                instruction_list.extend(expression_instructions)
            instruction_list.append(TwoOperandInstruction(self.symbol_table[identifier.attribute], OperatorType.ASSIGNMENT, result))
        elif current_node.node_type == NodeType.IF:
            expression = current_node.children[0]
            post_if_label = Label()
            end_label = Label()
            result, expression_instructions = self.get_expression_instructions(expression)
            if expression_instructions:
                instruction_list.extend(expression_instructions)
            if_instruction = TwoOperandInstruction(result, OperatorType.JNTR, post_if_label)
            statement = current_node.children[1]
            statement_instructions = self.get_statement_instructions(statement)
            instruction_list.append(if_instruction)
            instruction_list.extend(statement_instructions)
            if len(current_node.children) > 2:
                instruction_list.append(TwoOperandInstruction(None, OperatorType.JUMP, end_label))
            instruction_list.append(post_if_label)
            if len(current_node.children) > 2:
                else_instructions = self.get_statement_instructions(current_node.children[2])
                instruction_list.extend(else_instructions)
                instruction_list.append(end_label)
        elif current_node.node_type == NodeType.WHILE:
            start_label = Label()
            end_label = Label()
            expression = current_node.children[0]
            instruction_list.append(start_label)
            result, expression_instructions = self.get_expression_instructions(expression)
            if expression_instructions:
                instruction_list.extend(expression_instructions)
            condition_instruction = TwoOperandInstruction(result, OperatorType.JNTR, end_label)
            instruction_list.append(condition_instruction)
            statement = current_node.children[1]
            statement_instructions = self.get_statement_instructions(statement)
            instruction_list.extend(statement_instructions)
            instruction_list.append(TwoOperandInstruction(None), OperatorType.JUMP, start_label)
            instruction_list.append(end_label)
        elif current_node.node_type == NodeType.COMPOSED:
            sequence_instructions = self.get_sequence_instructions(current_node)
            instruction_list.extend(sequence_instructions)
        return instruction_list

    def get_expression_instructions(self, current_node):
        """
        :type current_node:TreeNode|Token
        :rtype (Register|Token, list[TwoOperandInstruction])
        """
        if isinstance(current_node, TreeNode):
            if current_node.node_type in (
            NodeType.RELATION_EQUAl, NodeType.RELATION_NON_EQUAL, NodeType.RELATION_GREATER,
            NodeType.RELATION_GREATER_EQUAL, NodeType.RELATION_LESS, NodeType.RELATION_LESS_EQUAL):
                instruction_list = []
                left_expression = current_node.children[0]
                left_op, left_op_instructions = self.get_simple_expression_instructions(left_expression)
                if left_op_instructions:
                    instruction_list.extend(left_op_instructions)
                right_expression = current_node.children[1]
                right_op, right_op_instructions = self.get_simple_expression_instructions(right_expression)
                if right_op_instructions:
                    instruction_list.extend(right_op_instructions)
                result_register = Register()
                if current_node.node_type == NodeType.RELATION_EQUAl:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.RELATION_EQUAl, right_op))
                elif current_node.node_type == NodeType.RELATION_NON_EQUAL:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.RELATION_NON_EQUAL, right_op))
                elif current_node.node_type == NodeType.RELATION_LESS:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.RELATION_LESS, right_op))
                elif current_node.node_type == NodeType.RELATION_LESS_EQUAL:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.RELATION_LESS_EQUAL, right_op))
                elif current_node.node_type == NodeType.RELATION_GREATER:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.RELATION_GREATER, right_op))
                elif current_node.node_type == NodeType.RELATION_GREATER_EQUAL:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.RELATION_GREATER_EQUAL, right_op))
                return result_register, instruction_list
            else:
                return self.get_simple_expression_instructions(current_node)
        else:
            return self.symbol_table[current_node.attribute], None

    def get_simple_expression_instructions(self, current_node):
        """
        :type current_node:TreeNode|Token
        :rtype (Register|Token, list[TwoOperandInstruction])
        """
        if isinstance(current_node, TreeNode):
            if current_node.node_type in (
            NodeType.OPERATOR_UNARY_PLUS, NodeType.OPERATOR_UNARY_MINUS, NodeType.OPERATOR_PLUS,
            NodeType.OPERATOR_MINUS, NodeType.OPERATOR_OR):
                instruction_list = []
                left_expression = current_node.children[0]
                left_op, left_op_instructions = self.get_simple_expression_instructions(left_expression)
                if left_op_instructions:
                    instruction_list.extend(left_op_instructions)
                result_register = Register()
                if current_node.node_type == NodeType.OPERATOR_UNARY_PLUS:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, None,
                                                                    OperatorType.OPERATOR_UNARY_PLUS, left_op))
                    return result_register, instruction_list
                elif current_node.node_type == NodeType.OPERATOR_UNARY_MINUS:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, None,
                                                                    OperatorType.OPERATOR_UNARY_MINUS, left_op))
                    return result_register, instruction_list
                right_expression = current_node.children[1]
                right_op, right_op_instructions = self.get_simple_expression_instructions(right_expression)
                if right_op_instructions:
                    instruction_list.extend(right_op_instructions)
                if current_node.node_type == NodeType.OPERATOR_PLUS:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_PLUS, right_op))
                elif current_node.node_type == NodeType.OPERATOR_MINUS:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_MINUS, right_op))
                elif current_node.node_type == NodeType.OPERATOR_OR:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_OR, right_op))
                return result_register, instruction_list
            else:
                return self.get_term_instructions(current_node)
        else:
            return self.symbol_table[current_node.attribute], None

    def get_term_instructions(self, current_node):
        """
        :type current_node:TreeNode|Token
        :rtype (Register|Token, list[TwoOperandInstruction])
        """
        if isinstance(current_node, TreeNode):
            if current_node.node_type in (NodeType.OPERATOR_DIVISION, NodeType.OPERATOR_MULTIPLY, NodeType.OPERATOR_DIV,
                                          NodeType.OPERATOR_MOD, NodeType.OPERATOR_AND):
                instruction_list = []
                left_expression = current_node.children[0]
                left_op, left_op_instructions = self.get_simple_expression_instructions(left_expression)
                if left_op_instructions:
                    instruction_list.extend(left_op_instructions)
                right_expression = current_node.children[1]
                right_op, right_op_instructions = self.get_simple_expression_instructions(right_expression)
                if right_op_instructions:
                    instruction_list.extend(right_op_instructions)
                result_register = Register()
                if current_node.node_type == NodeType.OPERATOR_DIVISION:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_DIVISION, right_op))
                elif current_node.node_type == NodeType.OPERATOR_MULTIPLY:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_MULTIPLY, right_op))
                elif current_node.node_type == NodeType.OPERATOR_DIV:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_DIV, right_op))
                elif current_node.node_type == NodeType.OPERATOR_MOD:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_MOD, right_op))
                elif current_node.node_type == NodeType.OPERATOR_AND:
                    instruction_list.append(ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, left_op,
                                                                    OperatorType.OPERATOR_AND, right_op))
                return result_register, instruction_list
            else:
                return self.get_factor_instructions(current_node)
        else:
            return self.symbol_table[current_node.attribute], None

    def get_factor_instructions(self, current_node):
        """
        :type current_node:TreeNode|Token
        :rtype (Register|Token, list[TwoOperandInstruction])
        """
        if isinstance(current_node, TreeNode):
            instruction_list = []
            if current_node.node_type == NodeType.OPERATOR_NOT:
                left_expression = current_node.children[0]
                left_op, left_op_instructions = self.get_factor_instructions(left_expression)
                if left_op_instructions:
                    instruction_list.extend(left_op_instructions)
                result_register = Register()
                instruction_list.append(
                    ThreeOperandInstruction(result_register, OperatorType.ASSIGNMENT, None, OperatorType.OPERATOR_NOT,
                                            left_op))
                return result_register, instruction_list
            else:
                return self.get_expression_instructions(current_node)
        else:
            return self.symbol_table[current_node.attribute], None
