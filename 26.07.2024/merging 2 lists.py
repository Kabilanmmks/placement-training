def merge_sorted_lists(list1, list2):
    sorted_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    sorted_list.extend(list1[i:])
    sorted_list.extend(list2[j:])
    return sorted_list
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
