# Learning Projects

This is the repository where I store my Python learning projects.

## System Dependencies 
* Python 3


## 1. Guess-the-Number Game

This program is an interactive Guess-the-Number quiz where users attempt to guess a randomly generated number between 1 and 100. The program provides feedback on each guess and offers the ability to replay the game or exit at any time.

### Features

- **Random Number Generation:**
  - The program generates a random number between 1 and 100 at the start of each game.

- **Input Validation:**
  - The user is required to input a valid integer between 1 and 100.
  - If the input is invalid (e.g., a non-numeric value or out of range), the program prompts the user to try again.

- **Game Feedback:**
  - After each guess, the program provides feedback:
    - If the guess is too high: `"Try again! Your number is greater than mine."`
    - If the guess is too low: `"Try again! Your number is less than mine."`

- **Winning Message:**
  - When the user correctly guesses the number, the program displays a congratulatory message and the number of rounds it took to guess correctly.

- **Replay Option:**
  - After each successful game, users are prompted to play again or exit:
    - If the user inputs `"YES"`, a new game starts.
    - If the user inputs `"NO"`, the program thanks the user and exits.

- **Graceful Exit:**
  - The user can type `"STOP"` at any point during the game to interrupt and exit. The program displays a friendly goodbye message.

- **Error Handling:**
  - The program includes exception handling to manage unexpected errors, ensuring a smooth user experience.

### Program Flow

1. The game begins with a welcome message, explaining the rules and providing instructions on how to exit.
2. A random number between 1 and 100 is generated.
3. The user repeatedly guesses the number:
   - The program validates the input and gives feedback if the guess is incorrect.
   - When the correct number is guessed, the program congratulates the user and shows the number of attempts.
4. The user can choose to replay or exit.
5. The program ends gracefully with a goodbye message if the user chooses to stop or after exiting.

### Example Interaction

```plaintext
Welcome to the Guess-the-Number quiz!
Input your guess: it should be a number from 1 to 100.
Type "STOP" to exit at any time.
50
Try again! Your number is greater than mine.
25
Try again! Your number is less than mine.
30
Congratulations! You've guessed it!
Rounds played: 3

Would you like to play again? Print "YES" or "NO": NO
Thank you for playing! Goodbye!
```

# 2. Magic Ball Program 🎱

The **Magic Ball Program** is a fun and interactive application that simulates the classic Magic 8 Ball toy. Ask any question, and the Magic Ball will provide you with an insightful answer. Whether you're looking for guidance, humor, or just some lighthearted fun, this program is here to entertain!

## Features 

- **Interactive Question and Answer Process:** Ask your questions, and the Magic Ball will respond with one of 20 unique and predefined answers.
- **Personalized Experience:** Introduces itself and greets users by name for a friendly interaction.
- **Replay Option:** Users can ask as many questions as they'd like or choose to exit the program at any time.

## Program Flow

1. The program starts by greeting the user and asking for their name.
2. Users can then type in any question they have.
3. The Magic Ball provides a randomized answer from its pool of 20 responses, ranging from positive to uncertain to negative.
4. After receiving an answer, users can choose to ask another question or exit the program.

## Example Interaction 

```plaintext
Hi, friend! I am a Magic Ball. I know the answers to any of your questions. What's your name?
> Alex
Hi, Alex! It's nice to meet you.

What question did you come to me with?
> Will I succeed in my project?
You asked: Will I succeed in my project.
Let's have a look... Most likely.

Would you like to ask me again? Type YES or NO.
> NO
Thank you for the game! Don't take it too personally :) See you!
```