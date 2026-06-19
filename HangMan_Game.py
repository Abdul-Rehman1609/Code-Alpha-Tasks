import random

words = ["python", "apple", "school", "coding", "laptop"]
word = random.choice(words)

guessed = ""
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\n", display)

    if "_" not in display:
        print("You Win!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed += guess
        print("Correct!")
    else:
        chances -= 1
        print("Wrong! Attempts left:", chances)

if chances == 0:
    print("Game Over!")
    print("The word was:", word)