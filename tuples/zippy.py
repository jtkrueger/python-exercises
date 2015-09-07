# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.


def combo(list1, list2):
    list1 = list(list1)
    list2 = list(list2)
    list1_tuple = ()
    output = []

    for item in enumerate(list1):
        list1_tuple = (item[1], list2[item[0]])
        print(list1_tuple)
        output.append(list1_tuple)
    print(output)
    return output



        
        
        
combo(['swallow', 'snake', 'parrot'], 'abc')
