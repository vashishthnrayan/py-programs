import random
playing = True
number= random.randint(10, 20)
hero=0

print("I will generate a number between 10 and 20, and you have to guess it.one digit at a time.")
print("the game will end when you have a hero")
while playing:
    guess = int(input("Enter a number between 10 and 20:\n"))
    if number == guess:
        print("you win the game")
        print("the number is", number)
        hero += 1
        print("you have", hero, "hero")
        playing = False
    
    else:
        print("your guess isn't quite right, try again\n")
    
        print("you have", hero, "hero")