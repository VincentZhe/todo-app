
# while True:
#     user_enter = input('Want to add, show, edit, complete or exit?')

#     match user_enter:
#         case 'add':
#             action = input('Enter your action') + "\n"

#             # file = open('todos.txt', 'r')
#             # todos = file.readlines()
#             # file.close()

#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()

#             todos.append(action)
            
#             # file= open('todos.txt', 'w')
#             # file.writelines(todos)
#             # file.close() #better to close it

#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)

#         case 'show':
#             # for item in todos: 
#             # file = open('todos.txt', 'r')
#             # todos = file.readlines()
#             # file.close()

#             #better way with file open
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()

#             new_todos = [item.strip("\n") for item in todos]
            
#             for index, item in enumerate(new_todos):
#                 row = f"{index + 1}-{item}"
#                 print(row)
#         case 'edit':
#             number = int(input('Enter the number of list you want to edit'))
#             number = number - 1

#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()

#             new_todo = input('Enter the new to do')
#             todos[number] = new_todo + "\n"

#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         case 'complete':
#             number = int(input('Enter the number of list you want to complete'))

#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()

#             todos.pop(number - 1)

#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         case 'exit':
#             break
#         case whatever:
#             print('You enter the wrong command')

# print('over')            



# # IF Else
# while True:
#     user_enter = input('Want to add, show, edit, complete or exit?')
#     user_enter = user_enter.strip()
    
#     # if 'add' in user_enter or 'new' in user_enter or 'more' in user_enter:
#     if user_enter.startswith('add'):
#         action = user_enter[4:]

#                 # file = open('todos.txt', 'r')
#                 # todos = file.readlines()
#                 # file.close()

#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()

#         todos.append(action + '\n')
                
#                 # file= open('todos.txt', 'w')
#                 # file.writelines(todos)
#                 # file.close() #better to close it

#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)

#     # elif 'show' in user_enter:
#     elif user_enter.startswith('show'):
#                 # for item in todos: 
#                 # file = open('todos.txt', 'r')
#                 # todos = file.readlines()
#                 # file.close()

#                 #better way with file open
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()

#         new_todos = [item.strip("\n") for item in todos]
                
#         for index, item in enumerate(new_todos):
#             row = f"{index + 1}-{item}"
#             print(row)
#     # elif 'edit' in user_enter:
#     elif user_enter.startswith('edit'):
#         try:
#             number = int(user_enter[5:])
#             number = number - 1

#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()

#                 new_todo = input('Enter the new to do')
#                 todos[number] = new_todo + "\n"

#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         except ValueError:
#             print("Your command is not valid")
#             # user_enter = input('Want to add, show, edit, complete or exit?')
#             # user_enter = user_enter.strip()
#             continue        
#     # elif 'complete' in user_enter:
#     elif user_enter.startswith('complete'):
#         try:    
#             number = int(user_enter[9:])

#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()

#                 todos.pop(number - 1)

#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         except IndexError:
#             print("No item with that number")
#             continue        
#     # elif 'exit' in user_enter:
#     elif user_enter.startswith('exit'):
#         break
#     else:
#         print('You enter the wrong command')

# print('over')            


# Functions

# import functions -> functions.get_todos()
# from module import functions
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is" + now)

while True:
    user_enter = input('Want to add, show, edit, complete or exit?')
    user_enter = user_enter.strip()
    
    # if 'add' in user_enter or 'new' in user_enter or 'more' in user_enter:
    if user_enter.startswith('add'):
        action = user_enter[4:]

                # file = open('todos.txt', 'r')
                # todos = file.readlines()
                # file.close()

        todos = get_todos()

        todos.append(action + '\n')
                
                # file= open('todos.txt', 'w')
                # file.writelines(todos)
                # file.close() #better to close it

        write_todos(todos)

    # elif 'show' in user_enter:
    elif user_enter.startswith('show'):
                # for item in todos: 
                # file = open('todos.txt', 'r')
                # todos = file.readlines()
                # file.close()

                #better way with file open
        todos = get_todos()

        new_todos = [item.strip("\n") for item in todos]
                
        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
    # elif 'edit' in user_enter:
    elif user_enter.startswith('edit'):
        try:
            number = int(user_enter[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter the new to do')
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            # user_enter = input('Want to add, show, edit, complete or exit?')
            # user_enter = user_enter.strip()
            continue        
    # elif 'complete' in user_enter:
    elif user_enter.startswith('complete'):
        try:    
            number = int(user_enter[9:])

            todos = get_todos()

            todos.pop(number - 1)

            write_todos(todos)
        except IndexError:
            print("No item with that number")
            continue        
    # elif 'exit' in user_enter:
    elif user_enter.startswith('exit'):
        break
    else:
        print('You enter the wrong command')

print('over') 


     