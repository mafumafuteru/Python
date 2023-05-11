import random

COLORS = ["RED","ORANGE","YELLOW","GREEN","BLUE","PURPLE"]
CODE = [random.choice(COLORS) for a in range(4)] 

for i in range(12):
        guess = input("Please write four colors in the order you think(in upper case and seperate with spaces): ") .split()
        correct = 0
        for j in range(4):
                if guess[j]== CODE[j]:
                        correct += 1
        if correct == 4:
                print("Congrats! You break the code!")
                break
        else:
                print (f"Only {correct} colors are correct.")
else:
       print("Sorry, you run out of the chances to guess!") 
