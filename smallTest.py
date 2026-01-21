import array
import random

colors = ["orange","black","white","blue","red","green", "yellow", "purple", "pink"]


def colorChooser():
    color = random.choice(colors)
    return color

hello = colorChooser()

print(hello)

#change log #1:
#def colorChooser():
    #color = random.choice(colors)
    #root.config(bg=color)
    #instruction_label1.configure(text = f"This color in russian is called {root.cget('bg')}", font =("Times New Roman", 12))
    #return color
#  """ here i have the full function, including the return color, however in the gui.py file i have removed the return color as i haven't neeeded it. i've been using the
#      function like a void function """