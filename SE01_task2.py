import random

COLORS = ["RED","ORANGE","YELLOW","GREEN","BLUE","PURPLE"]
CODE = [random.choice(COLORS) for a in range(4)] 

for i in range(12):
        guess = input("Please write four colors in the order you think(in upper case and seperate with spaces): ") .split()
        if len(guess) != 4 or not all(color in COLORS for color in guess):
            print("Please write FOUR VALID colors from the list: ", COLORS)
            continue
        correct = 0
        misplaced = 0
        #covert guess to a set to remove the duplicates
        guess_set = set(guess)

        for j in guess_set:
               if j in CODE:
                      #only count each color once
                      if guess.count(j) <= CODE.count(j):
                             misplaced += min(guess.count(j), CODE.count(j))
        for j in range(4):
                if guess[j]== CODE[j]:
                        correct += 1
                        #remove from misplaced count if it's also correct
                        misplaced -= 1
        if correct == 4:
                print("Congrats! You break the code!")
                break
        else:
                print(f"{correct} colors are correct and in the right positions!")
                print(f"{misplaced} colors are right color but in the wrong place!")
else:
       print("Sorry, you run out of the chances to guess!") 
       print(f"The correct code is:{''.join(CODE)}")
