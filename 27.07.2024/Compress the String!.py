from itertools import groupby

def compress_string(s):
    grouped = groupby(s)
    
    result = ' '.join(f"({len(list(group))}, {key})" for key, group in grouped)
    
    return result


input_string = input().strip()
print(compress_string(input_string))
