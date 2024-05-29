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
        return self.root.find(key)

    def draw(self, x_spacing=25, y_spacing=30):
        turtle.speed(0)
        previous_level = []
        level = [self.root]
        level_counter = 0
        while True:
            # draw level
            turtle.penup()
            turtle.pencolor("black")
            turtle.goto(-x_spacing * (len(level) - 1) / 2, -level_counter * y_spacing)
            for node in level:
                if not node is None:
                    turtle.write(node.value, align="center", font=("Verdana", 15, "normal"))
                turtle.setheading(0)
                turtle.forward(x_spacing)

            # draw connections
            for node in level:
                if not node is None:
                    if not node.parent is None:
                        turtle.penup()
                        turtle.goto(-x_spacing * (len(level) - 1) / 2 + x_spacing * level.index(node),
                                    -level_counter * y_spacing)
                        turtle.pendown()
                        if node.parent.left_arm == node:
                            turtle.pencolor("red")
                        else:
                            turtle.pencolor("black")
                        turtle.goto(
                            -x_spacing * (len(previous_level) - 1) / 2 + x_spacing * previous_level.index(node.parent),
                            -level_counter * y_spacing + y_spacing)

            # iterate
            level_counter += 1
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
            previous_level = copy.copy(level)
            level = copy.copy(new_level)
            if not nodes_exist:
                return 0

    def append(self, value):
        self.root.append(value)

    def find_max(self):
        nodes = [self.root]
        values = []
        nodes_detected = True
        while nodes_detected:
            new_nodes = []
            nodes_detected = False
            for node in nodes:
                if not node is None:
                    nodes_detected = True
                    values.append(node.value)
                    new_nodes.append(node.right_arm)
                    new_nodes.append(node.left_arm)
            nodes = copy.copy(new_nodes)
        maximum = max(values)
        print(maximum)
        return self.find(maximum)
