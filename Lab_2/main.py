def insertions_sort(input_list):
    sorted_list = [input_list[0]]
    for i in range(1,len(input_list)):
        selected_value = input_list[i]
        inserted = False
        for ii in range(i):
            if selected_value<sorted_list[ii]:
                inserted = True
                sorted_list.insert(ii, selected_value)
                break
        if not inserted:
            sorted_list.append(selected_value)
    return sorted_list

print(insertions_sort([-1,10,20,3,40,-40]))
