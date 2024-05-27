from Node import Node
import turtle
import copy

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

    def draw(self):
        previous_level = []
        level = [self.root]
        level_counter = 0
        while True:
            # draw level
            turtle.penup()
            turtle.goto(-15 * (len(level) - 1), level_counter * 15)
            for node in level:
                if not node is None:
                    turtle.write(node.value, align="center")
                    turtle.setheading(90)
                    turtle.forward(30)

            # draw connections
            for node in level:
                if not node is None:
                    if not node.parent is None:
                        turtle.penup()
                        turtle.goto(-15 * (len(level) - 1) + 30 * level.index(node), level_counter * 15)
                        turtle.pendown()
                        turtle.goto(-15 * (len(previous_level) - 1) + 30 * previous_level.index(node.parent), level_counter * 15 - 15)

            # iterate
            nodes_exist = False
            new_level = []
            for node in level:
                if not node is None:
                    new_level.append(node.left_arm)
                    new_level.append(node.right_arm)
                    nodes_exist = True
                else:
                    new_level.append(None)
                    new_level.append(None)
            previous_level = level
            level = new_level

            if not nodes_exist:
                return 0