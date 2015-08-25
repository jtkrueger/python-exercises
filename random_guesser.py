import random

def turns_left(tries):
    if tries == 4:
        print('You have {} guess left!'.format(5 - tries))
    elif tries == 5:
        print("You ran out of guesses! I'll never tell you the random number!")
    else:
        print('You have {} guesses left.'.format(5 - tries)) 

def guess_game():
    print('Pick a whole number between 1 and 10. You have 5 guesses.')
    rand_int = random.randint(1, 10)
    guesses = range(0, 5)
    
    for i in guesses:
        guess = input('> ')
        tries = guesses[i] + 1

        try:
            guess_int = int(guess)
        except:
            print("That's not a whole number! Try Again.")
            print("BTW, that counts as a guess because fuck you, that's why.")
            turns_left(tries)
            continue

        if guess_int < 1 or guess_int > 10:
            print("I said between 1 and 10! Try Again")
            print("BTW, that counts as a guess because fuck you, that's why.")
            turns_left(tries)
            continue
        
        
        if guess_int == rand_int:
            print('You guessed right! The random number was {}'.format(rand_int))
            if tries == 1:
                print('It took you {} guess'.format(tries))
            else:
                print('It took you {} guesses'.format(tries))
            break
                      
        elif guess_int < rand_int:
            print('Too low! Guess higher')
            turns_left(tries)                  
            continue
                      
        elif guess_int > rand_int:
            print('Too high! Guess lower')
            turns_left(tries)
            continue

guess_game()
        

    
    
