# from tkinter import *
# import math
# from paragraphs import para
# import random
#
# window = Tk()
# window.title("Typing Speed")
# window.config(padx=100, pady=50)
#
# sentences = random.choice(para)
# total_words = int(len(sentences))
#
#
# def retrieve_input():
#     inputv = inputtxt.get("1.0", "end-1c")
#     print(inputv)
#     print(len(inputv))
#
#
# title_label = Label(text="Typing Speed")
# title_label.grid(column=1, row=0)
#
# txt = Text(window, height=5, width=30, bg="light yellow")
# txt.grid(column=1, row=1, )
# txt.insert(END, sentences)
#
# inputtxt = Text(window, height=5, width=30, bg="light grey")
# inputtxt.grid(column=1, row=2, )
#
# button = Button(window, height=2, width=10, text="esc", bg="light blue", command=retrieve_input)
# button.grid(column=1, row=3)
# print()
# # title_label.pack()
# # inputtxt.pack()
#
# window.mainloop()

word = "the car is moving"
user = input("User: ")

if user in word:
    print(len(user))
elif not(user in word):
    print("Misspelled words")
