class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        return self.word + '('+ self.meaning + ')'

flash = []
print("welcome to flashcard app")

while (True):
    word = input("Enter the name you want to add to flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(flashcard(word, meaning))
    option = input("enter 0,if you want to add more flashcards, or 1 to exit: ")

    if option :
        break

print("\nYour flashcards are:")
for i in flash:
    print(">", i)