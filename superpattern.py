'''This code is a game that prompts the user for inputs and will
draw different patterns according to those inputs'''

import pattern
import turtle
import math
import random

t = turtle.Turtle()

def main():
    # Setup pattern.py
    pattern.setup()

    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = input("Which mode do you want to play? 1, 2 or 3: ")

        # If they choose 'Rectangle Patterns'
        if mode == 1:
            centerX = input("What is the x point? ")
            centerY = input("What is the y point? ")
            offset = input("What is the offset? ")
            width = input("What is the width? ")
            height = input("What is the height? ")
            count = input("How many times should it repeat? ")
            rotation = input("What is the rotation? ")

            # Draw the rectangle pattern.py
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX = input("What is the x point? ")
            centerY = input("What is the y point? ")
            offset = input("What is the offset? ")
            radius = input("What is the radius? ")
            count = input("How many times should it repeat? ")

            # Draw the circle pattern.py
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            num = input("How many patterns do you want to make? ")
            if num == "":
                pattern.drawSuperPattern(1)
            else:
                pattern.drawSuperPattern(num)
         # Play again?

        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = input("Choose 1, 2, or 3: ")

        if response == 1:
            playAgain = True
        elif response == 2:
            pattern.reset()
        elif response == 3:
            playAgain = False
            print("Thanks for playing!")
            pattern.done()



main()