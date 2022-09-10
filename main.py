from tkinter import *
import pandas as pd
from random import choice, randint, shuffle

BACKGROUND_COLOR = "#B1DDC6"
#to make flip_card() functional we have to provide current_card as empty {} and make it global
current_card = {}
data_dict = {}

try:
    #we provide the path for the file with words that user doesn't know and wants to learn
    data = pd.read_csv(r'file path \data\words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv(r'file path \data\french_words.csv')
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    #make the current_card variable global needs for flip_card function
    # make flip_timer variable and make it global needs to functionality of the buttons
    global current_card, flip_timer

    # every time we go for new card by click on the buttons we invalidate the timer
    #passing the id of our flip_timer
    window.after_cancel(flip_timer)

    # #creating a dataframe from csv
    # data = pd.read_csv(r'PROJECTS\100days_of_code\TKinter\Flash_cards\data\french_words.csv')
    # #converting data frame to list of dictionaries with method orient="records"
    # data_dict = data.to_dict(orient="records")
   
   #random choice of the card from data_dict and taking value(word) by key "French"
    current_card = choice(data_dict)

    #to change the title in canvas method and show it on the card
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    
    #ro back to card_front we implement code and add fill="black" in the lines 24,25
    canvas.itemconfig(card_background, image=card_front)

    #when the buttoms clicked and new crad set up we need to setup a new flip_timer

    #to repeat the flip and setup new flip_timer 
    flip_timer = window.after(3000, func=flip_card)
        

def flip_card():
        #to change the title in canvas method and show it on the card
        canvas.itemconfig(card_title, text="English", fill="white")

        #to translate the French word in English and show it on the card
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")

        #to change the front_card to the back_card
        canvas.itemconfig(card_background, image=card_back) 


def words_to_learn():
    data_dict.remove(current_card)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv(r'file path \data\words_to_learn.csv', index=False)
    next_card()
     

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#timer --> after 3s change the parameters decribed in flip_card function
#flip timer variable needs to make it global 
# and setup new flip_timer inside next_card fuction, every time user clicked the buttons
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, heigh=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=r'file path \images\card_front.png')
card_back = PhotoImage(file=r'file path \images\card_back.png')
canvas.grid(column=0, row=0, columnspan=2)

#to place image in the center
card_background = canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400,150,text="Title", fill="black", font=("Arial", 35, "italic"))
card_word = canvas.create_text(400,263,text="word", fill="black", font=("Arial", 50,"bold"))

image_wrong = PhotoImage(file=r'file path \images\wrong.png')
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=2)
image_right = PhotoImage(file=r'file path \images\right.png')
button_right = Button(image=image_right, highlightthickness=0, command=words_to_learn)
button_right.grid(column=1, row=2)

#call next_card function to show card at the moment of code running
next_card()

window.mainloop()
