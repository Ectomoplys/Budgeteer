from transaction import Transaction
import commands as command
import pickle

def parse(command):
    print()
    command = command[0]

    if command == 'h' or command == 'help':
        command.help()
    elif command == 'a' or command == 'add':
        command.add(command[1:])
    elif command == 'd' or command == 'display':
        command.display()
    elif command == 'f' or command == 'find':
        command.find(command)
    elif command == 'q' or command == 'quit':
        command.quit()
        return False

    return True
















