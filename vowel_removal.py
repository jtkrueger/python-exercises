

print("Enter a word, I will remove the vowels for you.")

word = input("Your word is: ")

while True:
    word_list = list(word)

    try:
        word_list.remove('a')
        print(word_list)
        
    except:
        word_list.remove('3')
        break
    break
            


    

    
    
