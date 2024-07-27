n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation = input().split()[0]
    new_set = set(map(int, input().split()))
    
    if operation == 'intersection_update':
        A.intersection_update(new_set)
    elif operation == 'update':
        A.update(new_set)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(new_set)
    elif operation == 'difference_update':
        A.difference_update(new_set)
print(sum(A))
