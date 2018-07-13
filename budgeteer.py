from commandparse import parse_command


def main():
    starting = True

    while starting:
        command = input("command: ")
        commands = command.split()

        starting = parse_command(commands)

main()
