# Write your code here
import random

mylist = ['python', 'java', 'kotlin', 'javascript']
thought = list(random.choice(mylist))
operator = "play"
lives = 8
line = list(len(thought) * "-")
repeat = set()
# hyphen = (len(thought) - 3) * "-"

print('H A N G M A N')
while operator == "play":
    operator = input('Type "play" to play, "exit" to quit: > ')
    print('\n')
    # guess = input(f"Guess the word {thought[0] + thought[1] + thought[2] + hyphen}: > ")
    # print("You survived!" if guess == thought else "You lost!")
    while True:
        if "-" not in line:
            break
        print("".join(line))
        letter = input("Input a letter: ")
        if len(letter) > 1:
            print("You should input a single letter")
        elif letter.isupper() or letter.isalpha() == False:
            print("Please enter a lowercase English letter")
        elif letter in repeat:
            print("You've already guessed this letter")
        elif letter not in set(thought):
            print("That letter doesn't appear in the word")
            lives = lives - 1
            repeat.add(letter)
            if lives == 0:
                break
            print("\n")
        else:
            overidx = 0
            counter = thought.count(letter)
            for i in list(thought):
                if letter == i:
                    idx = (list(thought)).index(i)
                    line[idx] = letter
                    repeat.add(letter)
                    overidx = idx
            if counter > 1:
                for overidx, j in enumerate(thought):
                    idx = (list(thought)).index(j)
                    line[idx] = letter
                    overidx = idx
        if line.count("-") != 0:
            print("\n")
    if lives == 0:
        print("You lost!")
    else:
        print("You guessed the word!")
        print("You survived!")
    exit()

