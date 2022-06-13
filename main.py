import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess
import os
import sys

root = tk.Tk()

fSc = tk.IntVar()
sSc = tk.IntVar()
fNm = tk.StringVar()
sNm = tk.StringVar()
minute = tk.StringVar()

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

actionData = []
lastAction = ''

def lastActionReturn():
    global lastAction
    if lastAction == 'Gol':
        fd = open("scorers_table.txt", "r")
        d = fd.read()
        fd.close()
        m = d.split("\n")
        s = "\n".join(m[:-1])
        fd = open("scorers_table.txt", "w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()
    elif lastAction == 'Czerwona Kartka':
        fd = open("red_cards.txt", "r")
        d = fd.read()
        fd.close()
        m = d.split("\n")
        s = "\n".join(m[:-1])
        fd = open("red_cards.txt", "w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()
    elif lastAction == 'Zolta Kartka':
        fd = open("yellow_cards.txt", "r")
        d = fd.read()
        fd.close()
        m = d.split("\n")
        s = "\n".join(m[:-1])
        fd = open("yellow_cards.txt", "w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()

def playerSelect(a):
    selected_indices = playerList.curselection()
    print(selected_indices)
    selected = ",".join([playerList.get(i) for i in selected_indices])
    actionData.append(selected)

def actionSelect(b):
    selected_indices = actionList.curselection()
    selected = ",".join([actionList.get(i) for i in selected_indices])
    actionData.append(selected)

def actionFileWrite():
    global actionData
    global lastAction
    actionData = [ele for ele in actionData if ele.strip()]
    minuteSelected = minute.get()+"'"
    actionData.append(minuteSelected)
    if actionData[1] == 'Gol':
        scorers_table = open('scorers_table.txt', 'a')
        scorers_table.write('\n' + actionData[0] + ' ' + actionData[2])
        lastAction = 'Gol'
        actionData.clear()
    elif actionData[1] == 'Czerwona Kartka':
        red_cards = open('red_cards.txt', 'a')
        red_cards.write('\n' + actionData[0] + ' ' + actionData[2])
        lastAction = 'Czerwona Kartka'
        actionData.clear()
    elif actionData[1] == 'Zolta Kartka':
        yellow_cards = open('yellow_cards.txt', 'a')
        yellow_cards.write('\n' + actionData[0] + ' ' + actionData[2]   )
        lastAction = 'Zolta Kartka'
        actionData.clear()
    else:
        actionData.clear()

def contentClear():
    files = ['first_name.txt', 'first_score.txt','second_name.txt', 'second_score.txt', 'red_cards.txt', 'yellow_cards.txt', 'scorers_table.txt']
    for i in files:
        f = open(i, 'w')
        f.close()

def timerStart():
    p = subprocess.Popen([sys.executable, os.path.expanduser('~/PycharmProjects/scoreboard/timer.py')],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

def programStop():
    os.system('pkill -9 -f timer.py')

pixel = tk.PhotoImage(width=1, height=1)

root.title("scoreboard manager")

frame = tk.Frame(root)
frame.pack()

frame2 = tk.Frame(root)
frame2.pack(side=TOP)

frame2b = tk.Frame(root)
frame2b.pack(side=TOP)

frame2c = tk.Frame(root)
frame2c.pack(side=TOP,
             fill="x",
             pady=5)

frame3a = tk.Frame(root)
frame3a.pack(side=TOP)

name1 = tk.Label(frame,
                 text="Druzyna 1")
name1.grid(row=1, column=1)

e1 = tk.Entry(frame,
              textvariable=fNm)
e1.grid(row=1, column=2)

name2 = tk.Label(frame2,
                 text="Druzyna 2")
name2.grid(row=2, column=1)

e2 = tk.Entry(frame2,
              textvariable=sNm)
e2.grid(row=2, column=2)

score1 = tk.Label(frame,
                  text="Wynik")
score1.grid(row=1, column=3)

score1Entry = tk.Entry(frame,
                       textvariable=fSc)
score1Entry.grid(row=1, column=4)

score2 = tk.Label(frame2,
                  text="Wynik")
score2.grid(row=2, column=3)

score2Entry = tk.Entry(frame2,
                       textvariable=sSc)
score2Entry.grid(row=2, column=4)

btn = tk.Button(frame2b,
                text="Zaaktualizuj Wynik",
                command=refreshAction,
                image=pixel,
                height=30,
                width=152,
                compound="c"
                )
btn.grid(row=1, column=1)

btnTimer = tk.Button(frame2b,
                text="Wlacz Timer",
                command=timerStart,
                image=pixel,
                height=30,
                width=152,
                compound="c"
                )
btnTimer.grid(row=1, column=2)

btnTimer2 = tk.Button(frame2b,
                 text='Wylacz timer',
                 command=programStop,
                 image=pixel,
                 height=30,
                 width=152,
                 compound="c")
btnTimer2.grid(row=1, column=3, columnspan=5)

separator = ttk.Separator(frame2c,
                          orient='horizontal')
separator.pack(fill='x',
               side=BOTTOM)

playerList = ('Krzysztof Kowalski', 'Jan Debil', 'Robert Lewandowski', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan')
playerListVar = tk.StringVar(value=playerList)

actionList = ('Gol', 'Czerwona Kartka', 'Zolta Kartka')
actionListVar = tk.StringVar(value=actionList)

playerList = tk.Listbox(frame3a,
                        listvariable=playerListVar,
                        height=6,
                        selectmode='extended')
playerList.grid(row=2,
                column=1)
playerList.bind('<<ListboxSelect>>',
                playerSelect)

actionList = tk.Listbox(frame3a,
                        listvariable=actionListVar,
                        height=6,
                        selectmode='browse')
actionList.grid(row=2,
                column=2)
actionList.bind('<<ListboxSelect>>',
                actionSelect)

minuteEntry = tk.Entry(frame3a,
                       textvariable=minute)
minuteEntry.grid(row=2,
                 column=3,
                 sticky='N')

playerLabel = tk.Label(frame3a,
                       text='Wybierz Gracza',
                       font=('Helvetica', 14, 'bold'))
playerLabel.grid(row=1,
                 column=1)

actionLabel = tk.Label(frame3a,
                       text='Wybierz Akcje',
                       font=('Helvetica', 14, 'bold'))
actionLabel.grid(row=1,
                 column=2)

minuteLabel = tk.Label(frame3a,
                       text='Wpisz Minute',
                       font=('Helvetica', 14, 'bold'))
minuteLabel.grid(row=1,
                 column=3)

btn4 = tk.Button(frame3a,
                 text='Zatwierdz',
                 command=actionFileWrite,
                 image=pixel,
                 height=30,
                 width=182,
                 compound="c")
btn4.grid(row=2,
          column=3,
          sticky='')

btn5 = tk.Button(frame3a,
                 text='Cofnij',
                 command=lastActionReturn,
                 image=pixel,
                 height=30,
                 width=182,
                 compound="c")
btn5.grid(row=2,
          column=3,
          sticky='S')

btn6 = tk.Button(frame3a,
                 text='Reset danych',
                 command=contentClear,
                 image=pixel,
                 height=30,
                 width=152,
                 compound="c")
btn6.grid(row=3,
          column=0,
          columnspan=5)


root.mainloop()