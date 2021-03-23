import PySimpleGUI as gui
from subprocess import Popen
import sys
intext = gui.Input(key='mins')
layout = [[gui.Text("Enter desired length for you CPU stress test to run.")], [intext], [gui.Button('Okay')]]
window = gui.Window(title='CPU Stress Test', layout=layout, margins=(200, 200))
try:
    def min():
        mins = values['mins']
        Popen(["/home/harrypethan/Documents/Coding/cpu_stress_gui/cpu_stress.sh", mins])
    #ensures you can close it
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        elif event == "Okay":
            min()
            break
    window.close()
    sys.exit()
except:
    sys.exit()

