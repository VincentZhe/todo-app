import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My To Do App', layout=[[label], [input_box, add_button], [list_box, edit_button]], font=('Helvetica', 20))

while True:
    event, values = window.read()
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
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
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



