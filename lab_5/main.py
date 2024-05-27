"""
побудувати двійкове дерево пошуку з цілих чисел, що вводяться. Вивести його на екран у вигляді дерева.
Знайти вершину, яка містить задане число.
Визначити максимальний елемент в цьому дереві.
Алгоритм видалення елементу можна не реалізовувати.
"""

from Node import Node
from Tree import Tree

test = Tree(5)
test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(6)
test.append(7)
test.append(8)
test.append(9)
test.append(10)
test.draw()
input()