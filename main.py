import tkinter as tk
from tkinter import *
from tkinter import ttk

zawodnicy = ('Krzysztof Kowalski', 'Jan Kowalski', 'Robert Lewandowski', 'Jan Kowalski2', 'Jan Kowalski3')

root = tk.Tk()

fSc = tk.IntVar()
sSc = tk.IntVar()
fNm = tk.StringVar()
sNm = tk.StringVar()

rC = tk.StringVar()
yC = tk.StringVar()

def refreshAction():
    first_score = open('first_score.txt', 'w+')
    first_score.write(str(fSc.get()))
    first_score.close()

    second_score = open('second_score.txt', 'w+')
    second_score.write(str(sSc.get()))
    second_score.close()

    first_name = open('first_name.txt', 'w')
    first_name.write(str(fNm.get()))
    first_name.close()

    first_name = open('second_name.txt', 'w')
    first_name.write(str(sNm.get()))
    first_name.close()

def cards():
    red_cards = open('red_cards', 'a')
    red_cards.write(rC.get() + '\n')
    red_cards.close()

    yellow_cards = open('yellow_cards', 'a')
    yellow_cards.write(yC.get() + '\n')
    yellow_cards.close()

frame = tk.Frame(root)
root.title("scoreboard manager")
frame.pack()

frame2 = tk.Frame(root)
frame2.pack(side=TOP)

frame2b = tk.Frame(root)
frame2b.pack(side=TOP)

frame3 = tk.Frame(root)
frame3.pack(side=TOP)

frame4 = tk.Frame(root)
frame4.pack(side=TOP)

name1 = tk.Label(frame, text="Druzyna 1")
name1.pack(side=LEFT)

e1 = tk.Entry(frame, textvariable=fNm)
e1.pack(side=LEFT)

name2 = tk.Label(frame2, text="Druzyna 2")
name2.pack(side=LEFT)

e2 = tk.Entry(frame2, textvariable=sNm)
e2.pack(side=LEFT)

score1 = tk.Label(frame, text="Wynik")
score1.pack(side=LEFT)

score1Entry = tk.Entry(frame, textvariable=fSc)
score1Entry.pack(side=LEFT)

score2 = tk.Label(frame2, text="Wynik")
score2.pack(side=LEFT)

score2Entry = tk.Entry(frame2, textvariable=sSc)
score2Entry.pack(side=LEFT)

btn = tk.Button(frame2b, text="zaaktualizuj wynik", command=refreshAction)
btn.pack(side=BOTTOM)

sep = ttk.Separator(frame3, orient='horizontal')
sep.pack(fill='x',side=TOP)

redCard = tk.Label(frame3, text='Czerwona kartka [imie/nazwisko/minuta]')
redCard.pack(side=LEFT)
redCardEntry = tk.Entry(frame3, textvariable=rC)
redCardEntry.pack(side=LEFT)

yellowCard = tk.Label(frame4, text='Zolta kartka [imie/nazwisko/minuta]')
yellowCard.pack(side=LEFT)
yellowCardEntry = tk.Entry(frame4, textvariable=yC)
yellowCardEntry.pack(side=LEFT)

btn2 = tk.Button(text='zatwierdz', command=cards)
btn2.pack()

root.mainloop()