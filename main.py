from modules import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is ", now)
while True:
    user_action = input("type add,show,edit or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        # file = open('todos.txt','r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos() #filepath="todos.txt"

        todos.append(todo+'\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = functions.get_todos()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid. ")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There  is no item with that number.")
        except ValueError:
            print("Wrong input format entered!")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey,you entered an unknown command")

print("Bye!")
