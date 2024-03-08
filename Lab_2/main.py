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
            moved += sort_result[2]
            sublist = sort_result[0]
            for ii in range(len(sublist)):
                list_to_sort[ii * hk[iteration] + i] = sublist[ii]
    return [list_to_sort,compared,moved]

print('Сортування списку довжини 100')
unsorted_list = unsortgen(100)
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