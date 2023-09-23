from textblob import TextBlob
from tkinter import *


def correct_spelling():
    get_data = entry1.get()
    corr = TextBlob(get_data)
    data = corr.correct()

    entry2.delete(0, END)
    entry2.insert(0, data)


def main_window():
    global entry1, entry2

    win = Tk()
    win.geometry("500x370")
    win.resizable(False, False)
    win.config(bg="blue")
    win.title("Spell Corrector")

    Label1 = Label(
        win,
        text="Incorrect Spelling",
        font=("Tinos", 25, "bold"),
        bg="blue",
        fg="white",
    )
    Label1.place(x=100, y=20, height=50, width=300)

    entry1 = Entry(win, font=("Tinos", 20))
    entry1.place(x=50, y=80, height=50, width=400)

    Label2 = Label(
        win,
        text="Correct Spelling",
        font=("Tinos", 25, "bold"),
        bg="blue",
        fg="white",
    )
    Label2.place(x=100, y=140, height=50, width=300)

    entry2 = Entry(win, font=("Tinos", 20))
    entry2.place(x=50, y=200, height=50, width=400)

    button = Button(
        win, text="Done", font=("Tinos", 20), bg="yellow", command=correct_spelling
    )
    button.place(x=150, y=280, height=50, width=200)

    win.mainloop()


main_window()
