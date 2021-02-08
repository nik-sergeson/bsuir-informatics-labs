from TwoOperandInstruction import TwoOperandInstruction
from OperatorType import OperatorType


class ThreeOperandInstruction(TwoOperandInstruction):
    def __init__(self, first_operand, first_operator, second_operand, second_operator, third_operand):
        super(ThreeOperandInstruction, self).__init__(first_operand, first_operator, second_operand)
        self.second_operator = second_operator
        self.third_operand = third_operand

    def __str__(self):
        if self.second_operand:
            return "{0} {1} {2} {3} {4}".format(self.first_operand, OperatorType.operator_type_to_str(self.operator),
                                                self.second_operand,
                                                OperatorType.operator_type_to_str(self.second_operator),
                                                self.third_operand)
        else:
            return "{0} {1} {2} {3}".format(self.first_operand, OperatorType.operator_type_to_str(self.operator),
                                            OperatorType.operator_type_to_str(self.second_operator), self.third_operand)
