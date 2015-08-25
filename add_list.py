numbers = [3, 4, 5]

def add_list(list):
    total = 0
    for item in list:
        total += item
    print(total)

    
add_list(numbers)

def summarize(list):
  string_list = ' '.join(str(e) for e in list)
  print("The sum of " + string_list + " is " + str(add_list(list)))

summarize(numbers)
    
