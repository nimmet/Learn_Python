
import PySimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
inches_label = sg.Text("Enter inches: ")

feet_input = sg.InputText(key="feet")
inches_input = sg.InputText(key="inches")

convert = sg.Button("Convert")
sideNote = sg.Text(key="-output-")

window = sg.Window("Convertor",layout=[
    [feet_label, feet_input],
    [inches_label, inches_input],
    [convert,sideNote]
])


event, values = window.read()
result = float(values['feet']) + float(values['inches'])
sg.popup(result)
if event == "Convert":
    window['-output-'].update(float(values['feet']) + float(values['inches']))
window.close()