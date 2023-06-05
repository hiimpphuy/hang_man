import os
import random
import time
import keyboard

treasure_x = random.randint(0,2)
treasure_y = random.randint(0,2)
row1= [" ", " ", " "]
row2= [" ", " ", " "]
row3= [" ", " ", " "]
treasure_map = [row1,row2,row3]

while True:
    os.system('clear')
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where the treasure ?? ")
    if position == "q":
        break
    horizonal = int(position[0])
    vertical  = int(position[1])
    treasure_map[horizonal-1][vertical-1] = "X"
    if horizonal-1 == treasure_x and vertical-1 == treasure_y:
        treasure_map[horizonal - 1][vertical - 1] = "@"
        print("You find the treasure")
        print(f"{row1}\n{row2}\n{row3}")
        keyboard.wait('space')
        break
    else:
        print("Try again. You almost get it!!")
    time.sleep(2)
