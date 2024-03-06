import PythonTableConsole
import copy
import math
import random

def unsortgen(length):
    unsorted_list = list(range(length))
    for i in range(int(length/2)):
        pos_1 = int(random.random() * length)
        pos_2 = int(random.random() * length)
        unsorted_list[pos_1], unsorted_list[pos_2] = unsorted_list[pos_2], unsorted_list[pos_1]
    return unsorted_list

def insertions_sort(input_list):
    list_to_sort = copy.copy(input_list)
    for i in range(len(list_to_sort)):
        inserted = False
        for ii in range(i-1,-1,-1):
            if list_to_sort[i] >= list_to_sort[ii]:
                list_to_sort.insert(ii+1, list_to_sort[i])
                list_to_sort.pop(i + 1)
                inserted=True
                break
        if not inserted:
            list_to_sort.insert(0, list_to_sort[i])
            list_to_sort.pop(i+1)
    return list_to_sort

def logged_insertions_sort(input_list):
    Log_Table = PythonTableConsole.PythonTableConsole([input_list])
    Log_Table.transpose()
    list_to_sort = copy.copy(input_list)
    for i in range(len(input_list)):
        inserted = False
        for ii in range(i - 1, -1, -1):
            if list_to_sort[i] >= list_to_sort[ii]:
                list_to_sort.insert(ii + 1, list_to_sort[i])
                list_to_sort.pop(i + 1)
                inserted = True
                break
        if not inserted:
            list_to_sort.insert(0, list_to_sort[i])
            list_to_sort.pop(i + 1)


        for ii in range(len(list_to_sort)):
            Log_Table.contains[ii].append(list_to_sort[ii])
    return Log_Table


def selections_sort(input_list):
    list_to_sort = copy.copy(input_list)
    for i in range(len(list_to_sort)):
        minimum = min(list_to_sort[i:])
        index_of_minimum = list_to_sort.index(minimum)
        list_to_sort[i], list_to_sort[index_of_minimum] = list_to_sort[index_of_minimum],list_to_sort[i]
    return list_to_sort

def logged_selections_sort(input_list):
    log_table = PythonTableConsole.PythonTableConsole([input_list])
    log_table.transpose()
    list_to_sort = copy.copy(input_list)
    for i in range(len(list_to_sort)):
        minimum = min(list_to_sort[i:])
        index_of_minimum = list_to_sort.index(minimum)
        list_to_sort[i], list_to_sort[index_of_minimum] = list_to_sort[index_of_minimum],list_to_sort[i]
        for ii in range(len(list_to_sort)):
            log_table.contains[ii].append(list_to_sort[ii])
    return log_table

def shells_sort(input_list):
    list_to_sort = copy.copy(input_list)
    hk = [1]
    while True:
        new_hk_value = hk[0]*3+1
        if new_hk_value<len(input_list):
            hk.insert(0,new_hk_value)
        else:
            break
    for iteration in range(len(hk)):
        for i in range(hk[iteration]):
            sublist = list_to_sort[slice(i,len(list_to_sort),hk[iteration])]
            sublist = selections_sort(sublist)
            for ii in range(len(sublist)):
                list_to_sort[ii*hk[iteration]+i] = sublist[ii]
    return list_to_sort

def logged_shells_sort(input_list):
    log_table = PythonTableConsole.PythonTableConsole([input_list])
    log_table.transpose()
    list_to_sort = copy.copy(input_list)
    hk = [1]
    while True:
        new_hk_value = hk[0]*3+1
        if new_hk_value<len(input_list):
            hk.insert(0,new_hk_value)
        else:
            break
    for iteration in range(len(hk)):
        for i in range(hk[iteration]):
            sublist = list_to_sort[slice(i,len(list_to_sort),hk[iteration])]
            sublist = selections_sort(sublist)
            for ii in range(len(sublist)):
                list_to_sort[ii*hk[iteration]+i] = sublist[ii]
        for i in range(len(list_to_sort)):
            log_table.contains[i].append(list_to_sort[i])
    return log_table

print(logged_shells_sort(unsortgen(10)))