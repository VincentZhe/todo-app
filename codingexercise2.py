import FreeSimpleGUI as sg
from Converter import convert

label1 = sg.Text("Enter feet")
input1 = sg.Input(key='feet')

label2 = sg.Text("Enter inches")
input2 = sg.Input(key='incehs')

convert_button = sg.Button("Convert")

output_label = sg.Text("", key='result')

window = sg.Window("Convertor", layout=[[label1, input1], [label2, input2], [convert_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values['feet']) 
    inches = float(values['incehs'])
    result = convert(feet, inches)
    window['result'].update(value=result)
window.close()