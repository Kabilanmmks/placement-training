from math import comb

def calculate_probability(n, letters, k):
    count_a = letters.count('a')
    
    if count_a == 0:
        return 0.0
    
    total_combinations = comb(n, k)
    non_a_count = n - count_a
    
    
    if k > non_a_count:
        return 1.0  
    
    combinations_without_a = comb(non_a_count, k)
    
    
    probability_no_a = combinations_without_a / total_combinations
    probability_at_least_one_a = 1 - probability_no_a
    
    return probability_at_least_one_a

n = int(input().strip())
letters = input().strip().split()
k = int(input().strip())

result = calculate_probability(n, letters, k)

print(f"{result:.4f}")
