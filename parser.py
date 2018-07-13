from transaction import Transaction
import commands as command
import pickle

def parse(commands):
    _command = commands[0]

    if _command == 'help':
        command.help()
    elif _command == 'add':
        command.add(commands[1:])
    elif _command == 'display':
        command.display()
    elif _command == 'find':
        command.find(command)
    elif _command == 'quit':
        command.quit()
        return False

    return True
















