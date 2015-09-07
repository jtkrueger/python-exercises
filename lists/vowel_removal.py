

print("Enter a word, I will remove the vowels for you. Enter DONE to end script.")

while True:
    
    word = input("\nYour word is: ")
    word_list = list(word.lower())
    vowels = list('aeiou')
    output = ''

    if word == "DONE":
        print("\ncool")
        break

    for letter in word_list:
        for vowel in vowels:
            while True:
                try:
                    word_list.remove(vowel)
                except:
                    break
        output = ''.join(word_list)
        


    print(output)    
        

    
            


    

    
    
