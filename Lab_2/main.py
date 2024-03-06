import PythonTableConsole
import copy

unsorted_list = [1,4,2,7,-1,0,3,5,0]

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