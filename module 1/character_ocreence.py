string=input("Please enter your own word:")

char=input("Please enter the character you want to count:")
i=0
count=0
while (i<len(string)):

    if (string[i]==char):
        count+=1
    i+=1

print("The character", char, "occurs", count, "times in the word", string)