print("Lets play guess the number game. Please guess a number between 1 and 10: ")
while True:
    guess = int(input())
    if guess < 5:
        print("Please guess higher")
    elif guess > 5:
        print("Please guess lower.")
    else:
        print ("Well done, you guessed it")
        break