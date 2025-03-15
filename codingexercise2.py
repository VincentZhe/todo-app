import FreeSimpleGUI as sg
from Converter import convert

label1 = sg.Text("Enter feet")
input1 = sg.Input(key='feet')

label2 = sg.Text("Enter inches")
input2 = sg.Input(key='inches')

convert_button = sg.Button("Convert")

output_label = sg.Text("", key='result')

exit_button = sg.Button('Exit')

window = sg.Window("Convertor", layout=[[label1, input1], [label2, input2], [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            feet = float(values['feet'])
            inches = float(values['inches'])
            result = convert(feet, inches)
            window['result'].update(value=result)
        case 'Exit':
            break
window.close()