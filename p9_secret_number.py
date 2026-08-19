secret_number=7
while True:
    guess = int(input("Guess the number between 1 and 10:"))
    if guess==secret_number:
        print("CONGRATULATIONS! You guessed correctly!")
        break
    else:
        print("Wrong guess! Try again.")