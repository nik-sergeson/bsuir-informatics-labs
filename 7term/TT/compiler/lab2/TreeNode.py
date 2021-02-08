class TreeNode(object):
    """
    :type children: list[TreeNode]
    """
    def __init__(self, node_type, *children):
        self.node_type = node_type
        self.children = list(children)

    def append_children(self, *args):
        self.children.extend(args)
