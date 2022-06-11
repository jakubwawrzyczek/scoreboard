import tkinter as tk
from tkinter import *
from tkinter import ttk

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

kutas = []

def playerSelect(a):
    selected_indices = playerList.curselection()
    selected = ",".join([playerList.get(i) for i in selected_indices])
    kutas.append(selected)
def actionSelect(b):
    # get selected indices
    selected_indices = actionList.curselection()
    # get selected items
    selected = ",".join([actionList.get(i) for i in selected_indices])
    kutas.append(selected)
def actionFileWrite():
    minuteSelected =minute.get()+"'"
    kutas.append(minuteSelected)
    if kutas[1] ==
    print(kutas[0], kutas[3])
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
sep.pack(fill='x', side=TOP)

playerList = ('Krzysztof Kowalski', 'Jan Debil', 'Robert Lewandowski', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan')
playerListVar = tk.StringVar(value=playerList)

actionList = ('Gol', 'Czerwona Kartka', 'Zolta kartka')
actionListVar = tk.StringVar(value=actionList)

frame3.columnconfigure(0, weight=1)
frame3.columnconfigure(0, weight=1)

playerList = tk.Listbox(frame3, listvariable=playerListVar, height=6, selectmode='browse')
playerList.pack(side=LEFT)
playerList.bind('<<ListboxSelect>>', playerSelect)

actionList = tk.Listbox(frame3, listvariable=actionListVar, height=6, selectmode='browse')
actionList.pack(side=LEFT)
actionList.bind('<<ListboxSelect>>', actionSelect)

minuteEntry = tk.Entry(frame3, textvariable=minute)
minuteEntry.pack()

btn4 = tk.Button(frame4, text='zatwierdz', command=actionFileWrite)
btn4.pack(side=LEFT)

root.mainloop()