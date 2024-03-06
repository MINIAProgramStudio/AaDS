import PythonTableConsole
import copy
import math
import random


def unsortgen(length):
    unsorted_list = list(range(length))
    for i in range(int(length / 2)):
        pos_1 = int(random.random() * length)
        pos_2 = int(random.random() * length)
        unsorted_list[pos_1], unsorted_list[pos_2] = unsorted_list[pos_2], unsorted_list[pos_1]
    return unsorted_list


def selections_sort(input_list):
    compared = 0
    moved = 0
    list_to_sort = copy.copy(input_list)
    for i in range(len(list_to_sort)):
        minimum = min(list_to_sort[i:])
        index_of_minimum = list_to_sort.index(minimum)
        list_to_sort[i], list_to_sort[index_of_minimum] = list_to_sort[index_of_minimum], list_to_sort[i]
        compared += len(list_to_sort[i:])
        moved += 1
    return [list_to_sort, compared, moved]


def shells_sort(input_list):
    list_to_sort = copy.copy(input_list)
    compared = 0
    moved = 0
    hk = [1]
    while True:
        new_hk_value = hk[0] * 3 + 1
        if new_hk_value < len(input_list):
            hk.insert(0, new_hk_value)
        else:
            break
    for iteration in range(len(hk)):
        for i in range(hk[iteration]):
            sublist = list_to_sort[slice(i, len(list_to_sort), hk[iteration])]
            sort_result = selections_sort(sublist)
            compared += sort_result[1]
            compared += sort_result[2]
            sublist = sort_result[0]
            for ii in range(len(sublist)):
                list_to_sort[ii * hk[iteration] + i] = sublist[ii]
    return [list_to_sort,compared,moved]

