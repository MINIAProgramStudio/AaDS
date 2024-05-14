import handler
stack_1 = handler.Stack(list())
stack_1.put(1)
stack_1.put(2)
print(stack_1.take())
print(stack_1.take())

stack_2 = handler.Stack(handler.DoubleLinkedList(1))
stack_2.put(2)
print(stack_2.take())
print(stack_2.take())