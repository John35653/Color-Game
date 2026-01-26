import tkinter as tk
import random
from googletrans import Translator   

translator = Translator()
colors = ["orange","black","white","blue","red","green", "yellow", "purple", "pink"]

def colorChooser():
    color = random.choice(colors)
    root.config(bg=color)
    instruction_label1.configure(text = translator.translate(f"This color in russian is called {root.cget('bg')}\n What color is this in English?", dest='ru').text,\
    font =("Open Sans", 20))

title = translator.translate("Color Game",dest='ru').text

root = tk.Tk()
root.title(f"{title}")
root.geometry("1050x500")

root.configure(bg = "white")
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
                                                
instruction_label1 = tk.Label(root, text = translator.translate(f"This color in russian is called {root.cget('bg')}\n What color is this in English?",dest='ru').text,\
    font =("Open Sans", 20))
instruction_label1.grid(row=0,column=0,sticky="n",pady=40)

instruction_label2 = tk.Label(root, text = translator.translate("If you click next and the color does not change,\n just click the next button again", dest='ru').text,\
    font=("Open Sans", 14))
#instruction_label2.pack(pady = 60)
instruction_label2.grid(row=1, column=0, sticky="n", pady=10)

next_page = tk.Button(root, text = translator.translate("Next",dest='ru').text, font=("Tmes New Roman",20), command=colorChooser)
next_page.grid(row=2,column=0,sticky="n",padx=40, pady=40)

root.mainloop()