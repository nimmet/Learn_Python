import PySimpleGUI as sg 

s_file = sg.Text("Select files to compress:")
s_input = sg.InputText()
d_file = sg.Text("Select destination folder:")
d_input = sg.InputText()
filechooser = sg.FilesBrowse("Choose",key="files")
folderchooser = sg.FolderBrowse("Choose",key="folder")
compress = sg.Button("Compress")


window = sg.Window("File Zipper",layout=[[s_file,s_input,filechooser],
                                         [d_file,d_input,folderchooser],
                                         [compress]])

while True:
    event,values=window.read()
    print(values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
window.close()