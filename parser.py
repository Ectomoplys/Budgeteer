import commands as command
import error_handler
import argparse
import sys


def parse(commands):

    _command = commands[0]

    if _command == 'help':          
        command.help()
    elif _command == 'add':         
        command.add(commands[1:])
    elif _command == 'display':     # All done
                                    # TODO: Date
                                    # sort [date|cost]
        command.display()       
    elif _command == 'delete':      
        command.delete(commands[1])
    elif _command == 'find':        
        if len(commands) == 1:
            print('please enter criteria')
            return True

        command.find(commands[1:])
    elif _command == 'clear':
        command.clear()
    elif _command == 'test':
        command.test()
    elif _command == 'quit':        
        command.quit()
        return False

    return True





class Parser(object):

    def __init__(self):
        