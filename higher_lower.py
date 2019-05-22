# John Dunne (Jd5an)


import random
guess = "Guess a number: "
count = 0
answer = int(input("What should the answer be? "))
if answer == -1:
    answer = random.randint(1, 100)
tries = int(input("How many guesses? "))
while count != tries and guess != answer:
    guess = int(input("Guess a number: "))
    if guess < answer:
        count += 1
        if count < tries:
            print("The number is higher than that.")
    elif guess > answer:
        count += 1
        if count < tries:
            print("The number is lower than that.")
    if guess == answer:
        print("You win!")
if count == tries:
    print("You lose; the number was", str(answer))
