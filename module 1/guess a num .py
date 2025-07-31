import random
import time

NUMBER = random.randint(1, 100)

def intro():
    print("may I ask you name")
    global name
    name = input("Enter your name: ")
    print(name + ", we are going to play a game . I am thinking of a number between 1 and 100.")

if (NUMBER% 2 == 0):
    x = "even"
else:
    x = "odd"
print("\nThe is an {}number".format(x))
time.sleep(.5)
print("go ahead and guess the number")

def pick():
    guessesTaken=0

    while guessesTaken < 6:
        time.sleep(.25)
        enter =input("Enter your guess: ")

        try:
            guess=int(enter)

            if guess <= 100 and guess >= 1:
                guessesTaken=guessesTaken + 1
                if guessesTaken<6:
                    if guess < NUMBER:
                        print("Your guess is too low.")
                    if  guess > NUMBER:
                     print("Your guess is too high.")
                    if guess != NUMBER:
                        time    .sleep(.5)
                    print("try again")

                    if guess == NUMBER:
                        break
            if guess>100 or guess < 1:
                print("Silly Goose!That number is not between 1 and 100.")
                time.sleep(.25)
                print("plz enter a number between 1 and 100")
        except :
            print("I don't")