from ..lab2.NodeType import NodeType
from ..lab1.Type import Type


class TypeException(Exception):
    def __init__(self, expression_node, found, *expected):
        expected_types_str = ""
        for exp_type in expected:
            expected_types_str += Type.get_type_name(exp_type) + " "
        super(TypeException, self).__init__(
            "Wrong types in {0}: expected {1}, found {2}".format(NodeType.get_type_name(expression_node),
                                                                 expected_types_str,
                                                                 Type.get_type_name(found)))
