from tkinter import *
from random import *

# mainloop_0\1\2 used because I don't know how to pass arguments in Button commands.
# That's why I just defined various functions calling one mainloop() with different args.


def mainloop_0():
    mainloop(0)


def mainloop_1():
    mainloop(1)


def mainloop_2():
    mainloop(2)


def mainloop(answer: int):
    """Game logic.

    'answer' var depends on button, pressed by player.
    """
    value = randint(0, 2)

    if value == 0:
        bot_text = 'Камень'
    if value == 1:
        bot_text = 'Ножницы'
    if value == 2:
        bot_text = 'Бумага'

    if answer == 0:
        player_text = 'Камень'
    if answer == 1:
        player_text = 'Ножницы'
    if answer == 2:
        player_text = 'Бумага'

    if answer == (value + 4) % 3:
        bot_score_text.set(bot_score_text.get() + 1)
        result_label_text.set(player_text + ":" + bot_text + ".\nТы проиграл")
    if answer == (value + 2) % 3:
        player_score_text.set(player_score_text.get() + 1)
        result_label_text.set(player_text + ":" + bot_text + ".\nТы победил")
    if answer == value:
        result_label_text.set(player_text + ":" + bot_text + ".\nНичья")


if __name__ == '__main__':
    """There are 3 fields:
    
    1: score_frame
    2: main_frame with buttons
    3: result_label with game result
    """
    root = Tk()
    root.geometry('200x150')
    root.title('Камень, ножницы, бумага v1')

    score_frame = LabelFrame()

    player_score_text = IntVar()
    player_score_text.set(0)

    player_score = Label(master=score_frame, textvariable=player_score_text)
    player_score.grid(row=0, column=0)

    lbl_score = Label(master=score_frame, text=':')
    lbl_score.grid(row=0, column=1)

    bot_score_text = IntVar()
    bot_score_text.set(0)

    bot_score = Label(master=score_frame, textvariable=bot_score_text)
    bot_score.grid(row=0, column=2)

    score_frame.grid(row=0, column=0)

    main_frame = LabelFrame()

    rock = Button(master=main_frame, text='Камень', command=mainloop_0)
    scissors = Button(master=main_frame, text='Ножницы', command=mainloop_1)
    paper = Button(master=main_frame, text='Бумага', command=mainloop_2)

    rock.grid(row=0, column=1)
    scissors.grid(row=2, column=2)
    paper.grid(row=2, column=0)

    main_frame.grid(row=1, column=0)

    result_label_text = StringVar()
    result_label = Label(textvariable=result_label_text)
    result_label.grid(row=2, column=0)

    root.mainloop()