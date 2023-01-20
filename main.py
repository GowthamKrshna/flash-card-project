BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import pandas
import random

data = pandas.read_csv('data/french_words.csv')
new_word = data.to_dict(orient='records')
current_card={}
def next_card():
    global current_card, timer_flip
    window.after_cancel(timer_flip)
    current_card= random.choice(new_word)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    canvas.itemconfig(background, image= card_front_image)
    timer_flip = window.after(3500, func=flip_card)

def flip_card():
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')
    canvas.itemconfig(background, image= card_back_image)

window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer_flip = window.after(3500, func=flip_card)

canvas= tkinter.Canvas(width=800, height=526, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file='images/card_front.png')
card_back_image = tkinter.PhotoImage(file='images/card_back.png')
background = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))

right_img = tkinter.PhotoImage(file='images/right.png')
right_btn = tkinter.Button(image=right_img, highlightthickness=0,command=next_card)
right_btn.grid(column=0, row= 1)
left_img = tkinter.PhotoImage(file='images/wrong.png')
wrong_btn = tkinter.Button(image=left_img, highlightthickness=0,command=next_card)
wrong_btn.grid(column=1, row= 1)

next_card()
window.mainloop()