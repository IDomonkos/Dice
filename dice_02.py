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
              [sg.Text("Ide jön majd...", size=(40,1), key='TEXT')]]

window = sg.Window('Dice roller', layout, resizable=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    button_events = map(str, x)

    if event in button_events:
        rolls = []
        for i in range(1, int(event) + 1):
            rolls.append(random.randint(MIN, MAX))

        window['TEXT'].update(rolls)

window.close()
