from random import randint


def generator_one_to_hundred():  # Generate the random number between 1 and 100
    print(
        'Welcome to the Guess-the-number quiz! Input your guess:',
        'it should be a number from 1 to 100.',
        'Type "STOP" to exit at any time.'
    )
    return randint(1, 100)


# Checks if the user input is valid (integer and between 1 and 100)
def is_valid(user_num):
    if user_num.isdigit():
        user_num = int(user_num)
        return 1 <= user_num <= 100
    return False


def main():
    play_again = True

    while play_again:  # Loop to allow replaying the game
        num1 = generator_one_to_hundred()
        counter_of_rounds = 0

        while True:
            user_num = input()

            # Check if the user wants to stop the game
            if user_num.strip().upper() == "STOP":
                print('Game interrupted. Thank you for playing! Goodbye!')
                return

            if not is_valid(user_num):
                print(
                    'Invalid input! Please enter an integer between 1 and 100,',
                    'or type "STOP" to exit.'
                )
                continue  # Ask the user for valid input again
            else:
                counter_of_rounds += 1

            user_num = int(user_num)
            if user_num == num1:
                print(
                    "Congratulations! You've guessed it!",
                    f"\nRounds played: {counter_of_rounds}"
                )

                # Ask if the user wants to play again
                while True:  # Ensure the user enters a valid response
                    play_again_check = input(
                        '\nWould you like to play again? Print "YES" or "NO": '
                    ).strip().upper()
                    if play_again_check == 'NO':
                        play_again = False
                        print('Thank you for playing! Goodbye!')
                        return
                    elif play_again_check == 'YES':
                        print('\nStarting a new game...')
                        break
                    else:
                        print('Invalid input! Please type YES or NO.')
                break  # Exit the game loop for a new game

            elif user_num > num1:
                print('Try again! Your number is greater than mine.')
            elif user_num < num1:
                print('Try again! Your number is less than mine.')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
