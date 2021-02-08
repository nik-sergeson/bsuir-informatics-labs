from OperatorType import OperatorType

class TwoOperandInstruction(object):
    def __init__(self, first_operand, operator_type, second_operand):
        self.first_operand = first_operand
        self.operator = operator_type
        self.second_operand = second_operand

    def __str__(self):
        if self.operator in (OperatorType.JUMP, OperatorType.JNTR, OperatorType.JTR):
            if self.first_operand:
                return "{0} {1} {2}".format(OperatorType.operator_type_to_str(self.operator), self.first_operand,
                                    self.second_operand)
            else:
                return "{0} {1}".format(OperatorType.operator_type_to_str(self.operator), self.second_operand)
        else:
            return "{0} {1} {2}".format(self.first_operand, OperatorType.operator_type_to_str(self.operator),
                                    self.second_operand)
