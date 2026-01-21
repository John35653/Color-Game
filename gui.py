import tkinter as tk
import random
from googletrans import Translator
import backend   


colors = ["orange","black","white","blue","red","green", "yellow", "purple", "pink"]

def colorChooser():
    color = random.choice(colors)
    root.config(bg=color)
    instruction_label1.configure(text = f"This color in russian is called {root.cget('bg')}", font =("Times New Roman", 12))
    return color



#frontend logic:
root = tk.Tk()    #use game_title_translation 
root.title("Color Game")
root.geometry("1000x500")

#experiment = colorChooser()
root.configure(bg = "white")
                                                #use label one translation    use ru_name
instruction_label1 = tk.Label(root, text = f"This color in russian is called {root.cget('bg')}", font =("Times New Roman", 12))
instruction_label1.pack(pady = 20)
instruction_label1.place(x = 20, y = 40)

instruction_label2 = tk.Label(root, text = "What color is this in english?", font = ("Times New Roman", 12))
instruction_label2.pack(pady= 20)
instruction_label2.place(x = 20, y = 20)

entry = tk.Entry(root)
entry.pack(pady = 20)
entry.place(x=20, y=100)

submit_button = tk.Button(root, text = "Submit")
submit_button.pack(pady=20)
submit_button.place(x= 150, y=100, width=50, height=20)

user_answer = entry.get()

next_page = tk.Button(root, text = "Next", command=colorChooser)
next_page.pack(pady = 20)
next_page.place(x = 950, y = 450)

#previous_page = tk.Button(root, text = "Back")
#previous_page.pack(pady = 20)
#previous_page.place(x = 910, y = 450)
#answer_label = tk.Label(root, text = f"{user_answer}")
#answer_label.pack(pady=20)
root.mainloop()
