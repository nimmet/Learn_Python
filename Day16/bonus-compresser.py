import PySimpleGUI as sg 

s_file = sg.Text("Select files to compress:")
s_input = sg.InputText()
d_file = sg.Text("Select destination folder:")
d_input = sg.InputText()
filechooser = sg.FileBrowse("Choose")
folderchooser = sg.FolderBrowse("Choose")
compress = sg.Button("Compress")


window = sg.Window("File Zipper",layout=[[s_file,s_input,filechooser],
                                         [d_file,d_input,folderchooser],
                                         [compress]])
window.read()
window.close()