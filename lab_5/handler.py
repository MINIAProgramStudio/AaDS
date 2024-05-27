class Node:
    def __init__(self, value, parent = None, right_arm = None, left_arm = None):
        self.value = value
        self.parent = parent
        self.right_arm = right_arm
        self.left_arm = left_arm

    def __str__(self):
        return self.value

    def depth(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.depth() + 1

    def append(self, value):
        if self.right_arm is None:
            pass