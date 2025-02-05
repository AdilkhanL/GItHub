import random
Name = input("Hello! What is your name?\n")
print("Well, " + Name + ", I am thinking of a number between 1 and 20.\nTake a guess.\n")
ran = random.randrange(1, 20)
i = 0
cnt = 1
while i != 21:
    i = int(input())
    if i < ran:
        print("Your guess is too low.")
        cnt = cnt + 1
    if i > ran:
        print("Your guess is too high.")
        cnt = cnt + 1
    if i == ran:
        i = 21
print("Good job, " + Name + "! You guessed my number in " + str(cnt) + " guesses!")




'''
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
'''