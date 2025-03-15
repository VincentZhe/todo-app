import functions
import FreeSimpleGUI as sg
import time

#if no todos file
import os

#change the theme
sg.theme('Black')

#if no todos file, then create the todos file
if not os.path.exists("todos.txt"):
    with open ('todos.txt', 'w') as file:
        pass

#show the time
clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
# add_button = sg.Button("Add") #traditional button
add_button = sg.Button(size=2,image_source='add.png', mouseover_colors='LightBlue2', tooltip="Add Todo", key='todo')

list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

Complete_button = sg.Button("Complete")

Exit_button = sg.Button("Exit")

window = sg.Window('My To Do App', layout=[[clock],[label], [input_box, add_button],
                                           [list_box, edit_button, Complete_button],
                                           [Exit_button]], font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos']) # values[tods] give a list 
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break    


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



