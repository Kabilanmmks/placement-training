from collections import Counter

def most_frequent_char(s):
    if not s:
        return None
    count = Counter(s)
    return count.most_common(1)[0][0]

input_string = "hello"
print("Most frequent character:", most_frequent_char(input_string))
