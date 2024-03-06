import PythonTableConsole
import copy

unsorted_list = [1,4,2,7,-1,0,3,5]  # без повторів!!! Повтори ламають сортування :(
''' не подивився варіант (:
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
'''

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
print(logged_selections_sort(unsorted_list))