import PythonTableConsole
import copy

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

print(insertions_sort([1,3,2,0,-3,4]))