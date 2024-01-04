<<<<<<< HEAD
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
=======
hop = (i**2 for i in range(5))  # generator
top = [i**2 for i in range(5)]
print(top)
>>>>>>> 3ecf4b513fff3aa59e20c2c9d31b49d4a345bf55
