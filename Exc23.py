# generating colours
import random
from sty import fg


def generateRGB():
    red = random.randint(0, 256)
    blue = random.randint(0, 256)
    green = random.randint(0, 256)
    return red, blue, green


def generateColour(red, blue, green):
    return fg(red, blue, green)


red, blue, green = generateRGB()
colour = generateColour(red, blue, green)
print(colour, "Generating colours.")
