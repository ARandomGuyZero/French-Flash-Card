from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.create_text(150, 125, text="Some question text.", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img)
        self.true_btn.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()