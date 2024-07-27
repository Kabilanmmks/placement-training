def can_stack_cubes(cubes):
    left = 0
    right = len(cubes) - 1
    last = float('inf')

    while left <= right:
        if cubes[left] >= cubes[right]:
            current = cubes[left]
            left += 1
        else:
            current = cubes[right]
            right -= 1
    
        if current > last:
            return "No"
        
        last = current 

    return "Yes"

def main():
    T = int(input())
    results = []

    for _ in range(T):
        n = int(input())
        cubes = list(map(int, input().split()))
        result = can_stack_cubes(cubes)
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
