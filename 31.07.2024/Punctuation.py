import string

def remove_punctuation(s):
    return s.translate(str.maketrans("", "", string.punctuation))

input_string = "Hello, world!"
print("String without punctuation:", remove_punctuation(input_string))
