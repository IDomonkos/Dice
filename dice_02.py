import PySimpleGUI as sg
import random

MIN = 1
MAX = 6
x = range(1, 21)
dice_buttons = []

for i in x:
    dice_buttons.append(sg.Button(str(i)))

    layout = [dice_buttons,
          [sg.Button('Exit')],
          [sg.Text("Ide jön majd...", key='TEXT')]]

window = sg.Window('Dice roller', layout, resizable=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in ('1'):
        window['TEXT'].update(random.randint(MIN, MAX))

window.close()
