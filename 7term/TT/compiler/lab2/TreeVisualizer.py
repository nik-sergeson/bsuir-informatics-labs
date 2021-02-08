import networkx as nx
import matplotlib.pyplot as plt
from NodeType import NodeType
from TreeNode import TreeNode


class TreeVisualizer(object):
    def __init__(self, tree):
        self.tree = tree

    def traverse_graph(self, node, node_name):
        for child in node.children:
            if isinstance(child, TreeNode):
                child_name = "{0}.".format(self.counter) + NodeType.get_type_name(child)
                self.counter += 1
                self.G.add_node(child_name)
                self.G.add_edge(node_name, child_name)
                self.traverse_graph(child, child_name)
            else:
                child_name = "{0}.".format(self.counter) + child.__str__()
                self.counter += 1
                self.G.add_node(child_name)
                self.G.add_edge(node_name, child_name)

    def show_graph(self):
        self.G = nx.DiGraph()
        self.G.add_node("0.PROGRAM")
        self.counter = 1
        self.traverse_graph(self.tree, "0.PROGRAM")
        pos = nx.graphviz_layout(self.G, prog='dot')
        nodes=nx.draw_networkx_nodes(self.G, pos, with_labels=True, arrows=True, node_color='w')
        nodes.set_edgecolor('w')
        nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edges(self.G, pos, with_labels=True, arrows=False)
        plt.show()
