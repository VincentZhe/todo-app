import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To Do App', layout=[[label], [input_box, add_button]], font=('Helvetica', 20))
window.read()
window.close()

#How to push your code to github
# connect to your repository
#git remote add origin https://github.com/your-username/your-repo.git

# track all files
# git add .

# commit your changes
# git commit -m "Initial commit"

# if pushing for the first time
# git branch -M main
# git push -u origin main

# for the subsequent time
# git push



