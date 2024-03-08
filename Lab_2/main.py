import copy
import random
import time

def unsortgen(length):
    unsorted_list = list(range(length))
    for i in range(int(length / 2)):
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
    for gap in hk:
        for offset in range(gap):
            sublist = list_to_sort[slice(offset, len(list_to_sort), gap)]
            print('before:')
            print(sublist)
            for unsorted_element in range(0,len(sublist)):
                inserted = False
                for sorted_element in range(unsorted_element):
                    if sublist[unsorted_element] < sublist[sorted_element]:
                        sublist.insert(sorted_element, sublist[unsorted_element])
                        sublist.pop(unsorted_element+1)

                if not inserted:
                    sublist.append(sublist[unsorted_element])
                    sublist.pop(unsorted_element)
            print('after:')
            print(sublist)

    return [list_to_sort,compared,moved]

print('Сортування списку довжини 100')
unsorted_list = unsortgen(10)
print('Список: '+str(unsorted_list))
start = time.time()
sel_sor_100 = selections_sort(unsorted_list)
end = time.time()
sel_sor_100.append(end-start)
del(start)
del(end)
start = time.time()
she_sor_100 = shells_sort(unsorted_list)
end = time.time()
print('Сортований список:')
print(she_sor_100[0])
she_sor_100.append(end-start)
del(start)
del(end)
print('Сортування методом вибору:')
print('Порівнянь: '+str(sel_sor_100[1]))
print('Обмінів: '+str(sel_sor_100[2]))
print('Час виконання: '+str(sel_sor_100[3]))
print('Сортування методом Шелла:')
print('Порівнянь: '+str(she_sor_100[1]))
print('Обмінів: '+str(she_sor_100[2]))
print('Час виконання: '+str(she_sor_100[3]))
"""
print('Сортування списку довжини 1000')
unsorted_list = unsortgen(1000)
start = time.time()
sel_sor_1k = selections_sort(unsorted_list)
end = time.time()
sel_sor_1k.append(end-start)
del(start)
del(end)
start = time.time()
she_sor_1k = shells_sort(unsorted_list)
end = time.time()
she_sor_1k.append(end-start)
del(start)
del(end)
print('Сортування методом вибору:')
print('Порівнянь: '+str(sel_sor_1k[1]))
print('Обмінів: '+str(sel_sor_1k[2]))
print('Час виконання: '+str(sel_sor_1k[3]))
print('Сортування методом Шелла:')
print('Порівнянь: '+str(she_sor_1k[1]))
print('Обмінів: '+str(she_sor_1k[2]))
print('Час виконання: '+str(she_sor_1k[3]))

print('Сортування списку довжини 10k')
unsorted_list = unsortgen(10000)
start = time.time()
sel_sor_10k = selections_sort(unsorted_list)
end = time.time()
sel_sor_10k.append(end-start)
del(start)
del(end)
start = time.time()
she_sor_10k = shells_sort(unsorted_list)
end = time.time()
she_sor_10k.append(end-start)
del(start)
del(end)
print('Сортування методом вибору:')
print('Порівнянь: '+str(sel_sor_10k[1]))
print('Обмінів: '+str(sel_sor_10k[2]))
print('Час виконання: '+str(sel_sor_10k[3]))
print('Сортування методом Шелла:')
print('Порівнянь: '+str(she_sor_10k[1]))
print('Обмінів: '+str(she_sor_10k[2]))
print('Час виконання: '+str(she_sor_10k[3]))
"""
"""
print('Сортування списку довжини 100k')
unsorted_list = unsortgen(100000)
start = time.time()
sel_sor_100k = selections_sort(unsorted_list)
end = time.time()
sel_sor_100k.append(end-start)
del(start)
del(end)
start = time.time()
she_sor_100k = shells_sort(unsorted_list)
end = time.time()
she_sor_100k.append(end-start)
del(start)
del(end)
print('Сортування методом вибору:')
print('Порівнянь: '+str(sel_sor_100k[1]))
print('Обмінів: '+str(sel_sor_100k[2]))
print('Час виконання: '+str(sel_sor_100k[3]))
print('Сортування методом Шелла:')
print('Порівнянь: '+str(she_sor_100k[1]))
print('Обмінів: '+str(she_sor_100k[2]))
print('Час виконання: '+str(she_sor_100k[3]))
"""