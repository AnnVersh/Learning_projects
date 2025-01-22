"""
This program imitates a Magic Ball.
"""

from random import choice


def answer_questions():
    """Handles the Magic Ball's question and answer process."""
    answers = [
        "Undoubtedly.", "Pre-decided.", "No doubt about it.", "Definitely yes.",
        "You can be sure of it.", "It seems to me - yes.", "Most likely.", "Good prospects.",
        "The signs say - yes.", "Yes.", "It is not clear yet, try again.", "Ask later.",
        "Better not to tell...", "It cannot be predicted now.", "Concentrate and ask again.",
        "Don't even think about it.", "My answer is no.", "According to my data - no.",
        "Prospects are not very good.", "Very doubtful."
    ]

    while True:
        question = input("What question did you come to me with?\n")
        print(f"You asked: {question}.")
        print(f"Let's have a look... {choice(answers)}")
        print("Would you like to ask me again? Type YES or NO.")

        play_again = input().strip().upper()  # Normalize input
        if play_again == "YES":
            continue
        elif play_again == "NO":
            print("Thank you for the game! Don't take it too personally :) See you!")
            break
        else:
            print("Sorry, you typed something else. I guess you want to quit. Goodbye!")
            break


def main():
    """Greets the user and starts the Magic Ball interaction."""
    print("Hi, friend! I am a Magic Ball. "
          "I know the answers to any of your questions. "
          "What's your name?")

    user_name = input()
    print(f"Hi, {user_name}! It's nice to meet you.")
    answer_questions()


if __name__ == "__main__":
    main()
