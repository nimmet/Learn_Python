import PySimpleGUI as sg 

s_file = sg.Text("Select files to compress:")
s_input = sg.InputText()
d_file = sg.Text("Select destination folder:")
d_input = sg.InputText()
choose1 = sg.Button("Choose")
choose2 = sg.Button("Choose")
compress = sg.Button("Compress")


window = sg.Window("File Zipper",layout=[[s_file,s_input,choose1],
                                         [d_file,d_input,choose2],
                                         [compress]])
window.read()
window.close()