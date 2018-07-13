from transaction import Transaction
import pickle

transaction_list = []

def parse_command(commands):
    print()
    command = commands[0]

    global transaction_list

    if command == 'h' or command == 'help':
        __command_help()
    elif command == 'a' or command == 'add':
        __command_add(commands[1:])
    elif command == 'd' or command == 'display':
        __command_display()
    elif command == 'f' or command == 'find':
        __command_find(commands)
    elif command == 'q' or command == 'quit':
        __command_quit()
        return False

    print()
    return True


def __command_help():

    print("HELP")
    print('''
        ARGUMENT                RETURN TYPE     FUNCTION
        
-a [name] [cost] [isExpense?]   -> void         adds a new expense
-d [id]                         -> void         deletes a transaction
-s [name|cost|isExpense?]^      -> id           searches for a transaction
-q                              -> void         quits program
    ''')

def __command_find(commands):
    return


def __command_add(commands):

    nameflag = False
    costflag = False
    boolflag = False

    name = ""
    cost = 0.00
    isexpense = False

    index = 0

    isnotalpha = True

    while index < len(commands):

        command = commands[index]

        if not is_number(command) and isnotalpha:
            name += command + " "

        elif is_number(command) and isnotalpha:
            isnotalpha = False
            nameflag = True

        if is_number(command):
            cost = float(command)
            costflag = True

        if index == (len(commands) - 1):
            isexpense = True if (command == "Yes" or command == "yes" or command == "true" or command == "True") else False
            boolflag = True

        index += 1

    if not nameflag:
        name = input("name: ")

    if not costflag:
        cost = input("cost: ")

    if not boolflag:
        isexpense = input("isExpense?: ")

    transaction = Transaction(name, cost, isexpense)

    ## save_transaction(transaction)

    write_transaction_to_file(transaction)
    print('done')
    del transaction


def __command_display():
    '''
    transaction_list = load_transactions()

    for transaction in transaction_list:
        print(transaction)
    '''

    read_transactions_from_file()

def __command_quit():

    print("Goodbye!")


def is_number(n):

    try:
        float(n)
        return True
    except ValueError:
        return False


def save_transaction(transaction):

    with open('transaction_data.pkl', 'ab') as output:
        pickle.dump(transaction, output, pickle.HIGHEST_PROTOCOL)
        print("saving transaction")

    print("transaction saved")


def load_transactions():

    with open('transaction_data.pkl', 'rb') as input:
        while True:
            try:
                yield pickle.load(input)
            except EOFError:
                break

def write_transaction_to_file(transaction):
    file = open('transaction_history.txt', 'a+')

    file.write(transaction.__str__())

    file.close()

def read_transactions_from_file():
    file = open('transaction_history.txt', 'r')

    if file.mode == 'r':
        contents = file.read()
        print(contents)