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

actionData = []
lastAction = ''

def lastActionReturn():
    global lastAction


def playerSelect(a):
    selected_indices = playerList.curselection()
    print(selected_indices)
    selected = ",".join([playerList.get(i) for i in selected_indices])
    actionData.append(selected)
def actionSelect(b):
    # get selected indices
    selected_indices = actionList.curselection()
    # get selected items
    selected = ",".join([actionList.get(i) for i in selected_indices])
    actionData.append(selected)
def actionFileWrite():
    global actionData
    global lastAction
    actionData = [ele for ele in actionData if ele.strip()]
    minuteSelected = minute.get()+"'"
    actionData.append(minuteSelected)
    if actionData[1] == 'Gol':
        scorers_table = open('scorers_table', 'a')
        scorers_table.write(actionData[0] + ' ' + actionData[2] + '\n')
        lastAction = 'Gol'
        actionData.clear()
    elif actionData[1] == 'Czerwona Kartka':
        red_cards = open('red_cards', 'a')
        red_cards.write(actionData[0] + ' ' + actionData[2] + '\n')
        lastAction = 'Czerwona Kartka'
        actionData.clear()
    elif actionData[1] == 'Zolta Kartka':
        yellow_cards = open('yellow_cards', 'a')
        yellow_cards.write(actionData[0] + ' ' + actionData[2] + '\n')
        lastAction = 'Zolta Kartka'
        actionData.clear()
    else:
        actionData.clear()
frame = tk.Frame(root)
root.title("scoreboard manager")
frame.pack()

frame2 = tk.Frame(root)
frame2.pack(side=TOP)

frame2b = tk.Frame(root)
frame2b.pack(side=TOP)

frame2c = tk.Frame(root)
frame2c.pack(side=TOP,  fill="x", pady=5)

frame3a = tk.Frame(root)
frame3a.pack(side=TOP)

frame3b = tk.Frame(root)
frame3b.pack(side=TOP, pady=5)

frame4 = tk.Frame(root)
frame4.pack(side=BOTTOM)

frame5 = tk.Frame(root)
frame5.pack(side=BOTTOM)

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

btn = tk.Button(frame2b, text="Zaaktualizuj Wynik", command=refreshAction)
btn.pack(side=TOP)

separator = ttk.Separator(frame2c, orient='horizontal')
separator.pack(fill='x', side=BOTTOM)

playerList = ('Krzysztof Kowalski', 'Jan Debil', 'Robert Lewandowski', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan', 'Robert', 'Jan', 'Jan')
playerListVar = tk.StringVar(value=playerList)

actionList = ('Gol', 'Czerwona Kartka', 'Zolta Kartka')
actionListVar = tk.StringVar(value=actionList)

playerList = tk.Listbox(frame3b, listvariable=playerListVar, height=6, selectmode='extended')
playerList.pack(side=LEFT, padx=3)
playerList.bind('<<ListboxSelect>>', playerSelect)

actionList = tk.Listbox(frame3b, listvariable=actionListVar, height=6, selectmode='browse')
actionList.pack(side=LEFT, padx=3)
actionList.bind('<<ListboxSelect>>', actionSelect)

minuteEntry = tk.Entry(frame3b, textvariable=minute)
minuteEntry.pack(side=TOP, padx=1)

playerLabel = tk.Label(frame3a, text='Wybierz Gracza', font=('Helvetica', 14, 'bold'))
playerLabel.grid(row=1, column=1, padx=40)

actionLabel = tk.Label(frame3a, text='Wybierz Akcje', font=('Helvetica', 14, 'bold'))
actionLabel.grid(row=1, column=2, padx=40)

minuteLabel = tk.Label(frame3a, text='Wpisz Minute', font=('Helvetica', 14, 'bold'))
minuteLabel.grid(row=1, column=3, padx=40)

btn4 = tk.Button(frame3b, text='Zatwierdz', command=actionFileWrite)
btn4.pack(side=TOP)

btn5 = tk.Button(frame3b, text='Cofnij', command=lastActionReturn)
btn5.pack(side=TOP)

btn6 = tk.Button(frame5, text='Reset danych')
btn6.pack()

root.mainloop()