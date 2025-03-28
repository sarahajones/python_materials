import bulls_and_cows as bc


def main():
    # Please do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again = 'y'
    while (again == 'y'):
        play_game()
        again = input('would you like to play again? (y/n)')
    print('So long sucker!')


def play_game():
    ''' Plays a single interactive game of bulls and cows on the console'''
    answer = bc.generate_secret()
    bulls = 0
    count = 0
    while bulls < 4:
        count += count
        guess = input("Guess a four digit number please:")
        bulls = bc.how_many_bulls(guess, answer)
        cows = bc.how_many_cows(guess, answer)
        if bulls < 4:
            print(f"{bulls} bulls and {cows} cows")
        else:
            print(f"You got 4 bulls and win the game. It took {count} guesses")


# call the main function to run the game
main()
