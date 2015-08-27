a_string = "I am what I am"

def word_count(string_1):
    string_1 = string_1.lower().split()
    word_dict = {}
    for word_1 in string_1:
        if word_1 in word_dict:
            word_dict[word_1] += 1
        else:
            word_dict[word_1] = 1

    return word_dict
                
print(word_count(a_string))

