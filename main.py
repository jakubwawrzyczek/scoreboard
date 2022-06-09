import tkinter as tk
import os

root = tk.Tk()

while True:
    instruction = input('Wpisz działanie do wykonania, jeżeli potrzebujesz pomocy wpisz \"help\": ')
    instruction = instruction.split()
    if instruction[0] == 'first':
        if instruction[1] == 'setscore':
            first_score = open('first_score.txt', 'w+')
            first_score.write(instruction[2])
            first_score.close()
        elif instruction[1] == 'setname':
            first_name = open('first_name.txt', 'w')
            first_name.write(instruction[2])
            first_name.close()
        else:
            print('Nie rozpoznaje takiej instrukcji!')
    elif instruction[0] == 'second':
        if instruction[1] == 'setscore':
            second_score = open('second_score.txt', 'w+')
            second_score.write(instruction[2])
            second_score.close()
        elif instruction[1] == 'setname':
            second_name = open('second_name.txt', 'w')
            second_name.write(instruction[2])
            second_name.close()
        else:
            print('Nie rozpoznaje takiej instrukcji!')
    elif instruction[0] == 'timer':
        if instruction[1] == 'start':
            os.system('python timer.py')
        elif instruction[1] == 'reset':
            timer = open('timer.txt', 'w')
            timer.write('00:00')
        else:
            print('Nie rozpoznaje takiej instrukcji!')
    elif instruction[0] == 'warn':
        if instruction[1] == 'red':
            red_cards = open('red_cards', 'a')
            red_cards.write(instruction[2] + ' ' + instruction[3] + ' ' + instruction[4] + '\n')
            red_cards.close()
        elif instruction[1] == 'yellow':
            yellow_cards = open('yellow_cards', 'a')
            yellow_cards.writelines(instruction[2] + ' ' + instruction[3] + ' ' + instruction[4] + '\n')
            yellow_cards.close()
        elif instruction[1] == 'reset':
            yellow_cards = open('yellow_cards', 'w')
            red_cards = open('red_cards', 'w')
            red_cards.write('')
            yellow_cards.write('')
            yellow_cards.close()
            red_cards.close()

    else:
        print('Nie rozpoznaje takiej instrukcji!')

root.mainloop()

#async do obczajenia, jesli nie bedzie dzialac to z osobnego pliku huj dupa cycki dupa cyce wadowice