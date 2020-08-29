import re
import random
import tkinter as tk


word_list = ["cookie", "telescope", "robot", "couch", "australia", "zebra", "guitar", "python",
             "phosphorescent", "highway", "elevator", "woods", "cellar", "kangaroo", "poltergeist"]

# The pattern locks on a single alphabetical character.
regex = r"^[a-z]$"

lucky_number = 0
word = ""
steps = 0
door = "*"
answer = []


def format_answer():

    global answer

    # Returns the answer as a nice readale string.

    return "".join(answer)


def update_answer(letter):

    # We loop through the word to know the locations of the letter, and assign the same locations in the answer.

    global answer
    global word

    for index, item in enumerate(word):
        if item == letter:
            answer[index] = word[index]

    return format_answer()


def start_game():

    if playButton["text"] == "Play":
        playButton["text"] = "Guess a letter! :"
        playButton["state"] = 'disabled'

    set_new_game()


def check_letter():

    global steps
    global answer
    global word
    global regex

    letter = letterInput.get()

    if re.search(regex, letter):

        if (letter in word) and not (letter in answer):
            answerLabel[
                "text"] = f"Well done! For now, you've got {update_answer(letter)}"

        else:
            answerLabel[
                "text"] = f"Bad luck! Try again. For now, you've got {format_answer()}"

    steps += 1

    if door not in answer:
        answerLabel["text"] = f"Congratulations, you've guessed the word {format_answer()}. It took you 'only' {steps} guesses."


def set_new_game():
    global lucky_number
    global word
    global steps
    global answer
    global door

    lucky_number = random.randint(0, len(word_list)-1)
    word = word_list[lucky_number]
    steps = 0

    # We put as many placeholders as there are letters in the player's guess.
    answer = [door for i in range(len(word))]


window = tk.Tk()
window.geometry("500x500")
window.title("Z-Hangman")

frame1 = tk.Frame(window, width=200, height=100)
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(window, width=200, height=100)
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame3 = tk.Frame(window, width=200, height=100)
frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame4 = tk.Frame(window, width=200, height=100)
frame4.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame5 = tk.Frame(window, width=200, height=100)
frame5.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


titleLabel = tk.Label(
    frame1,
    text=f'Welcome to the Z-Hangman!',
    fg="black")
titleLabel.pack()

playButton = tk.Button(
    frame2,
    text=f"Play",
    fg="black",
    command=start_game,
    width=25,
    height=5)
playButton.pack()

answerLabel = tk.Label(
    frame3,
    text="Waiting...",
    width=50
)
answerLabel.pack(side=tk.LEFT)

letterInput = tk.Entry(frame4, width=1)
letterInput.pack(side=tk.LEFT)

validInput = tk.Button(
    frame4,
    text="Try",
    command=check_letter
)
validInput.pack(side=tk.LEFT)

quitButton = tk.Button(
    frame5,
    text="QUIT",
    fg="red",
    command=quit)
quitButton.pack()


window.mainloop()
