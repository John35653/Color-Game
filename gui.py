import tkinter as tk
import random
from googletrans import Translator   

translator = Translator()
colors = ["orange","black","white","blue","red","green", "yellow", "purple", "pink"]

def colorChooser():
    color = random.choice(colors)
    root.config(bg=color)
    instruction_label1.configure(text = translator.translate(f"This color in russian is called {root.cget('bg')}\n What color is this in English?", dest='ru').text,\
    font =("Times New Roman", 20))


    
title = translator.translate("Color Game",dest='ru').text


#frontend logic:
root = tk.Tk()    #use game_title_translation 
root.title(f"{title}")
root.geometry("1050x500")

#experiment = colorChooser()
root.configure(bg = "white")
                                                #use label one translation    use ru_name
instruction_label1 = tk.Label(root, text = translator.translate(f"This color in russian is called {root.cget('bg')}\n What color is this in English?",dest='ru').text,\
    font =("Times New Roman", 20))
instruction_label1.pack(pady = 20)
instruction_label1.place(x = 20, y = 40)

#   entry = tk.Entry(root)
#   entry.pack(pady = 20)
#   entry.place(x=20, y=100)
#   submit_button = tk.Button(root, text = "Submit")
#   submit_button.pack(pady=20)
#   submit_button.place(x= 150, y=100, width=50, height=20)

#user_answer = entry.get()

next_page = tk.Button(root, text = translator.translate("Next",dest='ru').text, font=("Tmes New Roman",20), command=colorChooser)
next_page.pack(pady = 20)
next_page.place(x = 850, y = 400)

#previous_page = tk.Button(root, text = "Back")
#previous_page.pack(pady = 20)
#previous_page.place(x = 910, y = 450)
#answer_label = tk.Label(root, text = f"{user_answer}")
#answer_label.pack(pady=20)
root.mainloop()
