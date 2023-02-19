name = "PySimpleGUI"
import functions
import PySimpleGUI as sg
from PySimpleGUI import __version__


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-DO App",
                   layout=[[label], [input_box,add_button]])
window.read()
window.close()