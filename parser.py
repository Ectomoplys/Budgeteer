import commands as command

def parse(commands):

    _command = commands[0]

    if _command == 'help':          # Done
        command.help()
    elif _command == 'add':         # Done
        command.add(commands[1:])
    elif _command == 'display':     # All done
                                    # TODO: Date
                                    # sort [date|cost]
        command.display()       
    elif _command == 'delete':      # Done
        command.delete(commands[1])
    elif _command == 'find':        # TODO
        if len(commands) == 1:
            print('please enter criteria')
            return True

        command.find(commands[1:])
    elif _command == 'clear':
        command.clear()
    elif _command == 'quit':        # Done
        command.quit()
        return False

    return True