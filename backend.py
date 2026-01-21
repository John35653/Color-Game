import random
import array
from googletrans import Translator 

score = 0

#dictionary of colors (color name : color code)
colors = ["orange","black","white","blue","red","green", "yellow", "purple", "pink"]


def colorChooser():
    color = random.choice(colors)
    return color



# def font_color(a):
#   if cName == "Red":
#       fontColor = "white"
#   elif cName == "Green":
#       fontColor == "white"
#   elif cName == "Yellow":
#       fontColor == "black"
#   elif cName == "Purple":
#       fontColor == "whtie"
#   elif cName == "Orange":
#       fontColor == "black"
#   elif cName == "Black":
#       fontColor == "white"
#   else:
#       fontColor == "black"
#   return fontColor

translator = Translator()

def translation(x):
    russian_translation = translator.translate(x,src='en', dest='ru')
    return russian_translation.text

#ru_name = translation(cName)
labelOne = "The color in Russian is called: "
labelOne_translation = translation(labelOne)
labelTwo = "What color is this in English: "
labelTwo_translation = translation(labelTwo)
game_title = "Color Game"
game_title_translation = translation(game_title)



#user_answer = input("What color is this? ").strip().lower
        
#   def answer_checker():
#       global score
#       if user_answer == cValue:
#           score += 1
#       else:
#           score = score
#       return score

