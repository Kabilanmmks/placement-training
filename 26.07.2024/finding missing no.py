def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    return total_sum - array_sum

print(find_missing_number([1, 2, 4, 5, 6], 6)) 
