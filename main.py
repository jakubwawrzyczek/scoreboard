import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess
import os
import sys

root = tk.Tk()

scoreA = 0
scoreB = 0
nameA = tk.StringVar()
nameB = tk.StringVar()
minute = tk.StringVar()

scoreAtxt = open('scoreA.txt', 'w')
scoreAtxt.write(str(scoreA))
scoreAtxt.close()



def refreshAction(): #refreshes team names in OBS
    first_name = open('teamA_name.txt', 'w')
    first_name.write(str(nameA.get()))
    first_name.close()

    second_name = open('teamB_name.txt', 'w')
    second_name.write(str(nameB.get()))
    second_name.close()

actionData = []
lastAction = ''
team = ''

def lastActionReturn(): #returns last submitted action
    global lastAction
    global team
    if team == 'a':
        if lastAction == 'Gol':
            fd = open("scorers_table_a.txt", "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open("scorers_table_a.txt", "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()

        elif lastAction == 'Czerwona Kartka':
            fd = open("red_cards_a.txt", "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open("red_cards_a.txt", "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()
        elif lastAction == 'Zolta Kartka':
            fd = open("yellow_cards_a.txt", "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open("yellow_cards_a.txt", "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()
    if team == 'b':
        if lastAction == 'Gol':
            fd = open("scorers_table_b.txt", "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open("scorers_table_b.txt", "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()

        elif lastAction == 'Czerwona Kartka':
            fd = open("red_cards_b.txt", "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open("red_cards_b.txt", "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()
        elif lastAction == 'Zolta Kartka':
            fd = open("yellow_cards_b.txt", "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open("yellow_cards_b.txt", "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()

def playerSelectA(a):
    global team
    selected_indices = playerListA.curselection()
    print(selected_indices)
    selected = ",".join([playerListA.get(i) for i in selected_indices])
    actionData.append(selected)
    team = 'a'
    print(selected)

def playerSelectB(a):
    global team
    selected_indices = playerListB.curselection()
    print(selected_indices)
    selected = ",".join([playerListB.get(i) for i in selected_indices])
    actionData.append(selected)
    team = 'b'
    print(selected)

def actionSelect(b):
    selected_indices = actionList.curselection()
    selected = ",".join([actionList.get(i) for i in selected_indices])
    actionData.append(selected)

def actionFileWrite(): #writes current name and minute to folder
    global actionData
    global lastAction
    global scoreA, scoreB
    actionData = [ele for ele in actionData if ele.strip()]
    minuteSelected = minute.get()+"'"
    actionData.append(minuteSelected)
    print(actionData)
    if team == 'a':
        if actionData[1] == 'Gol':
            scorers_table = open('scorers_table_a.txt', 'a')
            scorers_table.write('\n' + actionData[0] + ' ' + actionData[2])
            scorers_table.close()
            lastAction = 'Gol'
            actionData.clear()
            scoreA += 1
            scoreAtxt = open('scoreA.txt', 'w')
            scoreAtxt.write(str(scoreA))
            scoreAtxt.close()
        elif actionData[1] == 'Czerwona Kartka':
            red_cards = open('red_cards_a.txt', 'a')
            red_cards.write('\n' + actionData[0] + ' ' + actionData[2])
            red_cards.close()
            print('\n' + actionData[0] + ' ' + actionData[2])
            lastAction = 'Czerwona Kartka'
            actionData.clear()
        elif actionData[1] == 'Zolta Kartka':
            yellow_cards = open('yellow_cards_a.txt', 'a')
            yellow_cards.write('\n' + actionData[0] + actionData[2])
            yellow_cards.close()
            lastAction = 'Zolta Kartka'
            actionData.clear()
        else:
            actionData.clear()
    elif team == 'b':
        if actionData[1] == 'Gol':
            scorers_table = open('scorers_table_b.txt', 'a')
            scorers_table.write('\n' + actionData[0] + ' ' + actionData[2])
            scorers_table.close()
            lastAction = 'Gol'
            actionData.clear()
            scoreA += 1
            scoreAtxt = open('scoreA.txt', 'w')
            scoreAtxt.write(str(scoreB))
            scoreAtxt.close()
        elif actionData[1] == 'Czerwona Kartka':
            red_cards = open('red_cards_b.txt', 'a')
            red_cards.write('\n' + actionData[0] + ' ' + actionData[2])
            red_cards.close()
            lastAction = 'Czerwona Kartka'
            actionData.clear()
        elif actionData[1] == 'Zolta Kartka':
            yellow_cards = open('yellow_cards_b.txt', 'a')
            yellow_cards.write('\n' + actionData[0] + ' ' + actionData[2])
            yellow_cards.close()
            lastAction = 'Zolta Kartka'
            actionData.clear()
        else:
            actionData.clear()

def contentClear():
    files = ['teamA_name.txt', 'scoreA.txt','teamB_name.txt', 'scoreB.txt', 'red_cards_b.txt', 'yellow_cards_b.txt', 'red_cards_a.txt', 'yellow_cards_a.txt', 'scorers_table_a.txt', 'scorers_table_b.txt']
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
frame2.pack(side=TOP,
             fill="x",
             pady=5)

frame2b = tk.Frame(root)
frame2b.pack(side=TOP)

frame2c = tk.Frame(root)
frame2c.pack(side=TOP,
             fill="x",
             pady=5)

frame3a = tk.Frame(root)
frame3a.pack(side=TOP)

name1 = tk.Label(frame,
                 text="Team A")
name1.grid(row=1, column=1)

e1 = tk.Entry(frame,
              textvariable=nameA)
e1.grid(row=2, column=1)

name2 = tk.Label(frame,
                 text="Team B")
name2.grid(row=1, column=2)

e2 = tk.Entry(frame,
              textvariable=nameB)
e2.grid(row=2, column=2)

separator3 = ttk.Separator(frame2,
                          orient='horizontal')
separator3.pack(fill='x',
               side=BOTTOM)

btn = tk.Button(frame2b,
                text="Zaaktualizuj Nazwy",
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

playerListA = []
teamA = open('team_a_players.txt', 'r').readlines()
for i in teamA:
    i = i.strip()
    playerListA.append(i)
playerListVarA = tk.StringVar(value=playerListA)

playerListB = []
teamB = open('team_b_players.txt', 'r').readlines()
for i in teamB:
    i = i.strip()
    playerListB.append(i)
playerListVarB = tk.StringVar(value=playerListB)

actionList = ('Gol', 'Czerwona Kartka', 'Zolta Kartka')
actionListVar = tk.StringVar(value=actionList)

playerListA = tk.Listbox(frame3a,
                        listvariable=playerListVarA,
                        height=6,
                        selectmode='extended')
playerListA.grid(row=2,
                column=1)
playerListA.bind('<<ListboxSelect>>',
                playerSelectA)

playerListB = tk.Listbox(frame3a,
                        listvariable=playerListVarB,
                        height=6,
                        selectmode='extended')
playerListB.grid(row=2,
                column=2)
playerListB.bind('<<ListboxSelect>>',
                playerSelectB)

actionList = tk.Listbox(frame3a,
                        listvariable=actionListVar,
                        height=6,
                        selectmode='browse')
actionList.grid(row=2,
                column=3)
actionList.bind('<<ListboxSelect>>',
                actionSelect)

minuteEntry = tk.Entry(frame3a,
                       textvariable=minute)
minuteEntry.grid(row=2,
                 column=4,
                 sticky='N')

playerSelectA = tk.Label(frame3a,
                       text='Team A',
                       font=('Helvetica', 14, 'bold'))
playerSelectA.grid(row=1,
                 column=1)

playerSelectB = tk.Label(frame3a,
                       text='Team B',
                       font=('Helvetica', 14, 'bold'))
playerSelectB.grid(row=1,
                 column=2)

actionLabel = tk.Label(frame3a,
                       text='Wybierz Akcje',
                       font=('Helvetica', 14, 'bold'))
actionLabel.grid(row=1,
                 column=3)

minuteLabel = tk.Label(frame3a,
                       text='Wpisz Minute',
                       font=('Helvetica', 14, 'bold'))
minuteLabel.grid(row=1,
                 column=4)

btn4 = tk.Button(frame3a,
                 text='Zatwierdz',
                 command=actionFileWrite,
                 image=pixel,
                 height=30,
                 width=182,
                 compound="c")
btn4.grid(row=2,
          column=4,
          sticky='')

btn5 = tk.Button(frame3a,
                 text='Cofnij',
                 command=lastActionReturn,
                 image=pixel,
                 height=30,
                 width=182,
                 compound="c")
btn5.grid(row=2,
          column=4,
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