import parser


def main():
    starting = True

    while starting:
        command = input("command: ")
        commands = command.split(" ")

        starting = parser.parse(commands)

main()


