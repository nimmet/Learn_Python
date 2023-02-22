import PySimpleGUI as sg 
from zip_creator import make_archive

s_file = sg.Text("Select files to compress:")
s_input = sg.InputText()
d_file = sg.Text("Select destination folder:")
d_input = sg.InputText()
filechooser = sg.FilesBrowse("Choose",key="files")
folderchooser = sg.FolderBrowse("Choose",key="folder")
compress = sg.Button("Compress")
info = sg.Text("",key="info")

window = sg.Window("File Zipper",layout=[[s_file,s_input,filechooser],
                                         [d_file,d_input,folderchooser],
                                         [compress,info]])

while True:
    event,values=window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)
    window["info"].update(value="Compression completed!")
window.close()