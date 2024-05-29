"""
побудувати двійкове дерево пошуку з цілих чисел, що вводяться. Вивести його на екран у вигляді дерева.
Знайти вершину, яка містить задане число.
Визначити максимальний елемент в цьому дереві.
Алгоритм видалення елементу можна не реалізовувати.
"""

from Node import Node
from Tree import Tree
from random import random


def random_tree(nodes_n, min=0, max=99):
    width = max - min
    tree = Tree(int(random() * width + min))
    for n in range(nodes_n):
        value = int(random() * width + min)
        tree.append(value)
    return tree


test = random_tree(10)
print(test.find_max())
test.draw(35)
input()

