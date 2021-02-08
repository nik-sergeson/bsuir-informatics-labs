class OperatorType(object):
    ASSIGNMENT, RELATION_EQUAl, RELATION_NON_EQUAL, RELATION_LESS, RELATION_LESS_EQUAL, RELATION_GREATER, \
    RELATION_GREATER_EQUAL, OPERATOR_UNARY_PLUS, OPERATOR_UNARY_MINUS, OPERATOR_PLUS, OPERATOR_MINUS, OPERATOR_OR, \
    OPERATOR_MULTIPLY, OPERATOR_DIVISION, OPERATOR_DIV, OPERATOR_MOD, OPERATOR_AND, OPERATOR_NOT, JUMP, JTR, JNTR= range(21)

    type_names = [":=", "==", "!=", "<", "<=", ">", ">=", "+", "-", "+", "-", "or", "*", "/", "div", "mod", "and",
                  "not", "JMP", "JTR", "JNTR"]

    @classmethod
    def operator_type_to_str(cls, instruction_type):
        return cls.type_names[instruction_type]
