def count_words(s):
    words = s.split()
    return len(words)

input_string = "Hello world"
print("Number of words:", count_words(input_string))
