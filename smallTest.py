import array
import random

colors = ["orange","black","white","blue","red","green", "yellow", "purple", "pink"]


def colorChooser():
    color = random.choice(colors)
    return color

hello = colorChooser()

print(hello)