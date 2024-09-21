"""
French Flash Cards

Author: Alan
Date: September 18th 2024

This project opens a window where a random French word pops up in screen.
The user has three seconds to guess the word.
If they succeed, the word is removed from the list.
If not, the word is saved and can appear again.
This also generates a file called words_to_learn.csv, where it storages all the words the user hasn't guessed yet.
"""

from random import choice
from tkinter import Tk, Canvas, PhotoImage, Button

from pandas import read_csv, DataFrame
from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"

def get_csv_data():
    """
    Tries to get the words data from the words_to_learn.csv file.
    If it succeeds, then it returns the data as a dictionary.
    If not, it returns the default french_words data from the csv file.
    :return:
    """

    # Try getting the words from words_to_learn file
    try:
        # Get the words of the csv file to a Dataframe
        word_data = read_csv("data/words_to_learn.csv")
    # If the file doesn't exist, or the file is empty, we get the data from the default csv file
    except (FileNotFoundError, EmptyDataError):
        # Get the words of the csv file to a Dataframe
        word_data = read_csv("data/french_words.csv")

    # Convert the words to a dictionary
    return word_data.to_dict(orient="records")

def flip_card():
    """
    Changes the word's language to english
    :return:
    """
    # Gets the english word of the current_card
    english_word = current_card["English"]

    # Flips the card by changing image and text
    canvas.itemconfig(card_image, image=back_card_img)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_text, text=english_word)

def next_card():
    """
    Randomly gets a word from the dictionary, changes the card to front and gives the user 3 seconds to try and guess if they got it right.
    :return:
    """

    global card_flip_event, current_card, word_dict

    if card_flip_event:
        windows.after_cancel(card_flip_event)

    # Tries to choose a word, if the dictionary is not empty, it saves it into the current_card dictionary
    try:
        # Randomly choices a word
        current_card = choice(word_dict)
    except IndexError:
        # Gets new data from a csv file
        word_dict = get_csv_data()
        # Randomly choices a word
        current_card = choice(word_dict)
    finally:
        # Gets the word in French
        french_word = current_card["French"]

        # Gets a new card by changing image and text
        canvas.itemconfig(card_image, image=front_card_img)
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_text, text=french_word)

        # After 3 seconds, executes flip_card() function
        card_flip_event = windows.after(3000, flip_card)

def is_correct():
    """
    If it's correct, the word is removed from the list
    :return:
    """

    # Removes the word from the dictionary
    word_dict.remove(current_card)

    # Creates a new Dataframe and saves it into a csv file
    new_csv = DataFrame(word_dict)
    new_csv.to_csv("data/words_to_learn.csv", index=False)

    # Draws the next card
    next_card()

# Index of the event of the card flip
card_flip_event = None

# Current card data
current_card = {}

# Gets the word_dict data from a csv file
word_dict = get_csv_data()

windows = Tk()
windows.title("Flash cards")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(405, 265, image=front_card_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Starts by getting the flash card
next_card()

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=is_correct, highlightthickness=0)
right_button.grid(row=1, column=1)

windows.mainloop()
