import random
import os

#region initial_resource
lst_word = ["apple", "watermelon", "cherry", "pineapple","Grapes"]
word = random.choice(lst_word)
map = ["_" for i in word]
life = 5
lst_check = [i for i in word]
stm0 = "   ___________\
 \n    |/      | \
 \n    |      (_) \
 \n    |      \|/ \
 \n    |       | \
 \n    |      / \ \
 \n    | \
 \n ___|___"

stm1 = "   ___________\
 \n    |/      | \
 \n    |      (_) \
 \n    |      \|/ \
 \n    |       | \
 \n    |      \
 \n    | \
 \n ___|___"

stm2 = "   ___________\
 \n    |/      | \
 \n    |      (_) \
 \n    |      \|/ \
 \n    |       \
 \n    |      \
 \n    | \
 \n ___|___"

stm3 = "   ___________\
 \n    |/      | \
 \n    |      (_) \
 \n    |      \
 \n    |       \
 \n    |      \
 \n    | \
 \n ___|___"

stm4 = "   ___________\
 \n    |/      | \
 \n    |      \
 \n    |      \
 \n    |      \
 \n    |      \
 \n    | \
 \n ___|___"

stickman = [stm0,stm1,stm2,stm3,stm4]
#endregion

#region func-game
def check_word(letter_input,word,life):
    if letter_input in word:
        changeLettertoMap(letter_input,map,lst_check)
    else:
        life -= 1
        drawstickman(life,stickman)

def changeLettertoMap(letter_input,map,lst_check):
    changeLettertoMap.has_been_called = True
    for i in range(0,len(lst_check)):
        if letter_input == lst_check[i]:
            map[i] = letter_input
def drawstickman(life,stickman):
    drawstickman.has_been_called = True
    print(stickman[life])
if __name__ == '__main__':
    drawstickman.has_been_called = False
#endregion

#region MG

while True:
    os.system("clear")
    print(*map)
    letter_input = input("Guess it: ")
    check_word(letter_input,word,life)
    if drawstickman.has_been_called:
        drawstickman.has_been_called = False
        life -= 1
    if "".join(map) == word:
        print(word)
        print("Congratulations!!")
        break
    if life == 0:
        print("Your stickman is dead. Game Over!!")
        break
#endregion



