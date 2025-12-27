import random
# Generate random number
number = random.randint(1, 100)
# Number of attempts
attempts = 5
for i in range(attempts):
    guess = int(input("Guess the number (1 to 100): "))
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct! You guessed the number.")
        break
else:
    print("Game Over! The number was:", number)
