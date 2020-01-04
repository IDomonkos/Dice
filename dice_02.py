import PySimpleGUI as sg
import random

MIN = 1
MAX = 6

layout = [[sg.Button('1')]]

window = sg.Window('Dice roller', layout, resizable=True)

while True:
    event, values = window.read()
    if event in (None,):
        break
    if event in ('1'):

        print(random.randint(MIN, MAX))


window.close()