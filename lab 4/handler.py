class Stack:
    def __init__(self, container):
        self.container = container

    def put(self, element):
        self.container.append(element)

    def take(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            return None


# нижче код з 3ої лабораторної роботи
class Node:
    def __init__(self, contains, previous=None, next=None):
        self.contains = contains
        self.previous = previous
        self.next = next

    def __str__(self):
        return str(self.contains)


class DoubleLinkedList:
    def __init__(self, first_node_value=None):
        if first_node_value is None:
            self.first_node = None
            self.last_node = None
            self.length = 0
        else:
            first_node = Node(first_node_value)
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

    loop_active = False
    def update(self):
        self.length = 0
        selected_node = self.first_node
        self.loop_active = True
        while self.loop_active:
            if selected_node is None:
                self.loop_active = False
                break
            else:
                self.length += 1
                selected_node = selected_node.next
        if self.last_node == self.first_node and self.length > 1:
            self.last_node = selected_node

    def push(self, value):
        if self.first_node is None:
            self.first_node = Node(value)
            self.last_node = self.first_node
        else:
            node = Node(value)
            self.first_node.previous = node
            node.next = self.first_node
            node.previous = None
            self.first_node = node
        self.update()

    def append(self, value):
        if self.first_node is None:
            self.first_node = Node(value)
            self.last_node = self.first_node
        else:
            node = Node(value)
            self.last_node.next, node.previous, = node, self.last_node
            node.next = None
            self.last_node = node

    def pull(self):
        if len(self) < 1:
            self.update()
        if self.length == 0 or self.first_node is None:
            raise Exception("cannot pull from empty list")
        pulled_node = self.first_node
        self.first_node = self.first_node.next
        self.first_node.previous = None
        return pulled_node

    def pop(self, index = 0):
        self.update()
        if index >= self.length - 1:
            if self.length < 1:
                self.update()
            if self.length == 0 or self.last_node is None:
                raise Exception("cannot pop from empty list")
            popped_node = self.last_node
            self.last_node = self.last_node.previous
            self.last_node.next = None
            self.update()
            return popped_node
        if index == 0:
            return self.pull()
        if index >= self.length:
            raise Exception("index out of range")
        if index < self.length / 2:
            selected_node = self.first_node
            for i in range(0, index):
                selected_node = selected_node.next
            selected_node.previous.next, selected_node.next.previous = selected_node.next, selected_node.previous
        else:
            selected_node = self.last_node
            for i in range(0, self.length - index - 1):
                selected_node = selected_node.previous

            selected_node.previous.next, selected_node.next.previous = selected_node.next, selected_node.previous
        return selected_node

    def insert(self, value, index=0):
        if index >= self.length:
            raise Exception("index out of range")
        if self.first_node is None:
            self.first_node = Node(value)
            self.last_node = self.first_node
        else:
            node = Node(value)

            if index == 0:
                self.push(node)
            if index == self.length - 1:
                self.append(node)
            if index < self.length / 2:
                selected_node = self.first_node
                for i in range(0, index):
                    selected_node = selected_node.next
                selected_node.previous.next = node
                node.previous = selected_node.previous
                node.next = selected_node
                selected_node.previous = node
            else:
                selected_node = self.last_node
                for i in range(0, self.length - index):
                    selected_node = selected_node.previous
                selected_node.previous.next = node
                node.previous = selected_node.previous
                node.next = selected_node
                selected_node.previous = node
        self.update()

    def __getitem__(self, item):

        if not isinstance(item, int) or item >= self.length:
            print([item, self.length])
            raise Exception("index out of range")
        if item < self.length / 2:
            selected_node = self.first_node
            for i in range(0, item):
                selected_node = selected_node.next
        else:
            selected_node = self.last_node
            for i in range(0, self.length - item - 1):
                selected_node = selected_node.previous
        return selected_node

    def to_list(self):
        return_list = []
        selected_node = self.first_node
        while selected_node:
            return_list.append(selected_node.contains)
            selected_node = selected_node.next
        return return_list

    def __str__(self):
        string = ""
        self_list = self.to_list()
        for item in self_list:
            string += str(item)
        return string

    def __len__(self):
        self.update()
        return self.length

    def debug(self):
        selected_node = self.first_node
        while selected_node:
            print([selected_node.previous, selected_node, selected_node.next])
            if selected_node.next is None:
                break
            selected_node = selected_node.next

    def __sizeof__(self):
        size = 0
        for i in range(len(self)):
            size += sys.getsizeof(self[i])
        return size
