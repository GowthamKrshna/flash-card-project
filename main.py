BACKGROUND_COLOR = "#B1DDC6"
import tkinter


window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas= tkinter.Canvas(width=800, height=526, highlightthickness=0)
card_image = tkinter.PhotoImage(file='images/card_front.png')
canvas.create_image(105, 115, image= card_image)

language = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
language_text = canvas.create_text(400, 263, text='foo', font=('Ariel', 60, 'bold'))

right_img = tkinter.PhotoImage(file='images/right.png')
right_btn = tkinter.Button(image=right_img, highlightthickness=0)
right_btn.config()
left_img = tkinter.PhotoImage(file='images/left.png')
left_btn = tkinter.Button(image=left_img, highlightthickness=0)