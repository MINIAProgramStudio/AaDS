class Node:
    def __init__(self, contains, previous = None, next = None):
        self.contains = contains
        self.previous = previous
        self.next = next

    def __str__(self):
        return str(self.contains)

class DobleLinkedList:
    def __init__(self, first_node = None):
        if not isinstance(first_node,Node):
            raise Exception("first_node must be Node instance.")
        self.first_node = first_node
        self.length = 0
        if first_node:
            selected_node = first_node
            while True:
                self.length += 1
                if selected_node.next:
                    selected_node = selected_node.next
                else:
                    break
            self.last_node = selected_node

    def update(self):
        self.length = 0
        while True:
            self.length += 1
            if selected_node.next:
                if selected_node != selected_node.previous:
                    raise Exception("DoubleLinkedList is not doublelinked")
                selected_node = selected_node.next
            else:
                break
        if self.last_node != selected_node:
            raise Exception("DobleLinkedList last_node cannot be reached from first_node")