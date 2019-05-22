# John Dunne (Jd5an)

import random
print("Think of a number between 1 and 100 and I'll guess it.")
tries = int(input("How many guesses do I get? "))
count = 0
guess = 50
answer = "none"
highernum = 101
lowernum = 0
while count != tries and answer != "same" and int(highernum) != int(lowernum + 1):
    answer = input("Is the number higher, lower, or the same as " + str(guess) + "? ")
    if answer == "lower":
        highernum = guess
        count += 1
        if count != tries:
            if lowernum == "none":
                guess = random.randint(0, highernum)
            if lowernum != "none":
                guess = (lowernum + highernum)//2
    if answer == "higher":
        lowernum = guess
        count += 1
        if count != tries:
            if highernum == "none":
                guess = random.randint(lowernum, 101)
            if highernum != "none":
                guess = (lowernum + highernum) // 2
if highernum - 1 == lowernum:
    print("Wait; how can it be both higher than", str(lowernum), "and lower than", str(highernum) + "?")
if highernum - 1 == lowernum and count == tries:
    deceit = int(input("I lost; what was the answer? "))
    print("Wait; how can it be both higher than", str(lowernum), "and lower than", str(highernum) + "?")
if answer == "same":
    print("I won!")
if highernum - 1 != lowernum and count == tries:
    final_answer = int(input("I lost; what was the answer? "))
    if final_answer < lowernum or highernum == 100:
        print("That can't be; you said it was higher than", str(lowernum) + "!")
    elif final_answer > highernum or lowernum == 1:
        print("That can't be; you said it was lower than", str(highernum) + "!")
    elif final_answer > highernum:
        print("That can't be; you said it was lower than", str(highernum) + "!")
    elif final_answer < lowernum:
        print("That can't be; you said it was higher than", str(lowernum) + "!")
    elif highernum > final_answer > lowernum:
        print("Well played!")
