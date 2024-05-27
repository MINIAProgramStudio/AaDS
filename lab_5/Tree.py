from Node import Node

class Tree:
    def __init__(self, root):
        if isinstance(root, Node):
            self.root = root
        else:
            self.root = Node(root)

    def find(self, key):
        selected_node = self.root
        while True:
            if key < selected_node.value:
                selected_node = selected_node.left_arm
            elif key > selected_node.value:
                selected_node = selected_node.right_arm
            else:
                return selected_node
            if selected_node is None:
                return 0