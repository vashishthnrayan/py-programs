import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {
            'apple': 'Red',
            'banana': 'Yellow',
            'grape': 'Purple',
            'orange': 'Orange',
            'kiwi': 'Brown',
            'blueberry': 'Blue'
          
        }
    
    def quiz(self):
        while (True):

            fruit,color =random.choice(list(self.fruits.items()))

            print("what is the color of {}".format(fruit)) 
            user_answer = input()
            if( user_answer.lower() == color.lower()):
                print("Correct!")
            else:
                print("wrong answer")
            option = input("enter 0, if you want to continue the quiz, or 1 to exit: ")
            if option:
                break
print("welcome to the fruit quiz app")  

fq = FruitQuiz()
fq.quiz()