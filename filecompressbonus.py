import FreeSimpleGUI as sg

label1 = sg.Text("Select the file want to compress")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select the destination want to compress")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")


window = sg.Window('My File Compress', layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress_button]])
window.read()
window.close()