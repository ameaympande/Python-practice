guessNumber = 9
guessCount = 0
guessLimit = 3

print("Guess a number between 1 and 10")
while guessCount < guessLimit:
    guess = int(input("Guess :"))
    guessCount += 1
    if guess == guessNumber:
        print("You win !")
        break
else:
    print("Sorry you failed!")

