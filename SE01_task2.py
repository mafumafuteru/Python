import random

COLORS = ["RED","ORANGE","YELLOW","GREEN","BLUE","PURPLE"]
CODE = [random.choice(COLORS) for a in range(4)] 

for i in range(12):
        guess = input("Please write four colors in the order you think(in upper case and seperate with spaces): ") .split()
        correct = 0
        wrong_placed = 0
        for j in range(4):
                if guess[j]== CODE[j]:
                        correct += 1
                elif guess[j] in CODE:
                        wrong_placed += 1
        if correct == 4:
                print("Congrats! You break the code!")
                break
        else:
                print(f"{correct} colors are correct and in the right positions!")
                print(f"{wrong_placed} colors are right color but in the wrong postion!")
else:
       print("Sorry, you run out of the chances to guess!") 
