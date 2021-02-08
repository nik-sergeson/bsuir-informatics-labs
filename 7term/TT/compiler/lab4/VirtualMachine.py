from __future__ import division
from ..lab1.Type import Type
from ..lab1.Identifier import Identifier
from TwoOperandInstruction import TwoOperandInstruction
from ThreeOperandInstruction import ThreeOperandInstruction
from Register import Register
from Label import Label
from OperatorType import OperatorType


class VirtualMachine(object):
    def __init__(self):
        self.IP = 0
        self.registers = {}

    def execute(self, instructions, symbol_table):
        labels = {}
        for identifier in symbol_table:
            if isinstance(identifier, Identifier):
                if identifier.value is None:
                    if identifier.type == Type.BOOLEAN:
                        identifier.value = True
                    else:
                        identifier.value = 0
        while self.IP < len(instructions):
            instruction = instructions[self.IP]
            if isinstance(instruction, Label):
                labels[instruction.label] = self.IP + 1
            elif isinstance(instruction, TwoOperandInstruction):
                if isinstance(instruction.first_operand, Register):
                    if not instruction.first_operand.register in self.registers:
                        self.registers[instruction.first_operand.register] = instruction.first_operand
                if instruction.operator == OperatorType.ASSIGNMENT:
                    instruction.first_operand.value = instruction.second_operand.value
                elif instruction.operator == OperatorType.JNTR:
                    if not instruction.first_operand:
                        if instruction.second_operand.label in labels:
                            self.IP = labels[instruction.second_operand.label]
                            continue
                        else:
                            label_find = instruction.second_operand
                            while not (
                                isinstance(instructions[self.IP], Label) and instructions[self.IP] == label_find):
                                if isinstance(instructions[self.IP], Label):
                                    if not instructions[self.IP].label in labels:
                                        labels[instructions[self.IP].label] = self.IP + 1
                                self.IP += 1
                            self.IP += 1
                            continue
                elif instruction.operator == OperatorType.JUMP:
                    if instruction.second_operand.label in labels:
                        self.IP = labels[instruction.second_operand.label]
                        continue
                    else:
                        label_find = instruction.second_operand
                        while not (isinstance(instructions[self.IP], Label) and instructions[self.IP] == label_find):
                            if isinstance(instructions[self.IP], Label):
                                if not instructions[self.IP].label in labels:
                                    labels[instructions[self.IP].label] = self.IP + 1
                            self.IP += 1
                        self.IP += 1
                        continue
                elif instruction.operator == OperatorType.JTR:
                    if instruction.first_operand:
                        if instruction.second_operand.label in labels:
                            self.IP = labels[instruction.second_operand.label]
                            continue
                        else:
                            label_find = instruction.second_operand
                            while not (
                                isinstance(instructions[self.IP], Label) and instructions[self.IP] == label_find):
                                if isinstance(instructions[self.IP], Label):
                                    if not instructions[self.IP].label in labels:
                                        labels[instructions[self.IP].label] = self.IP + 1
                                self.IP += 1
                            self.IP += 1
                            continue
            elif isinstance(instruction, ThreeOperandInstruction):
                if isinstance(instruction.first_operand, Register):
                    if not instruction.first_operand.register in self.registers:
                        self.registers[instruction.first_operand.register] = instruction.first_operand
                if instruction.second_operator == OperatorType.RELATION_EQUAl:
                    instruction.first_operand = instruction.second_operand == instruction.third_operand
                elif instruction.second_operator == OperatorType.RELATION_NON_EQUAL:
                    instruction.first_operand = instruction.second_operand != instruction.third_operand
                elif instruction.second_operator == OperatorType.RELATION_LESS:
                    instruction.first_operand = instruction.second_operand < instruction.third_operand
                elif instruction.second_operator == OperatorType.RELATION_LESS_EQUAL:
                    instruction.first_operand = instruction.second_operand <= instruction.third_operand
                elif instruction.second_operator == OperatorType.RELATION_GREATER:
                    instruction.first_operand = instruction.second_operand > instruction.third_operand
                elif instruction.second_operator == OperatorType.RELATION_GREATER_EQUAL:
                    instruction.first_operand = instruction.second_operand >= instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_DIVISION:
                    instruction.first_operand = instruction.second_operand / instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_MULTIPLY:
                    instruction.first_operand = instruction.second_operand * instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_DIV:
                    instruction.first_operand = instruction.second_operand // instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_MOD:
                    instruction.first_operand = instruction.second_operand % instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_AND:
                    instruction.first_operand = instruction.second_operand and instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_NOT:
                    instruction.first_operand = not instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_UNARY_PLUS:
                    instruction.first_operand = +instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_UNARY_MINUS:
                    instruction.first_operand = -instruction.third_operand
                elif instruction.second_operator == OperatorType.OPERATOR_OR:
                    instruction.first_operand = instruction.second_operator or instruction.third_operand
            self.IP += 1
