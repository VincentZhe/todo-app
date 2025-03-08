def get_todos(filepath='todos.txt'): #default arguments
    with open(filepath, 'r') as file:
            todos = file.readlines()

    return todos

def write_todos(todos_arg,filepath='todos.txt'):
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)


# In here, __name__ represent the functions itself also called __main__
# IF in main.py to call this module, __name__ will become this module name, which is functions
print(__name__)

if __name__ == '__main__':
      print('Hello')
      print(get_todos())