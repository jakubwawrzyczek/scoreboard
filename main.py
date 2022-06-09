import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

fSc = tk.IntVar()
sSc = tk.IntVar()
fNm = tk.StringVar()
sNm = tk.StringVar()


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


frame = tk.Frame(root)
root.title("scoreboard manager")
frame.pack()

bottomFrame = tk.Frame(root)
bottomFrame.pack(side=TOP)

name1 = tk.Label(frame, text="Team 1")
name1.pack(side=LEFT)

e1 = tk.Entry(frame, textvariable=fNm)
e1.pack(side=LEFT)

name2 = tk.Label(bottomFrame, text="Team 2")
name2.pack(side=LEFT)

e2 = tk.Entry(bottomFrame, textvariable=sNm)
e2.pack(side=LEFT)

score1 = tk.Label(frame, text="Score")
score1.pack(side=LEFT)

e3 = tk.Entry(frame, textvariable=fSc)
e3.pack(side=LEFT)

score2 = tk.Label(bottomFrame, text="Score")
score2.pack(side=LEFT)

e4 = tk.Entry(bottomFrame, textvariable=sSc)
e4.pack(side=LEFT)

btn = tk.Button(text="refresh", command=refreshAction)
btn.pack()

root.mainloop()