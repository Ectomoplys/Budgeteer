import error_handler

def help():

    print("HELP")
    print('''
        ARGUMENT                RETURN TYPE     FUNCTION
-h                              -> string       displays help
-a  [name] [cost] [isExpense]   -> void         adds a new expense
-d  [id]                        -> void         deletes a transaction
-f  [name|cost|isExpense|date]  -> Transaction  searches for a transaction
-s  [date]                      -> string       displays list of transactions for certain date
    sort [date|cost]            -> string       displays list of transactions sorted by [argument] from low to high
    all                         -> string       displays all transactions
-q                              -> void         quits program
    ''')

def find(commands):
    return


def add(input):
    name = ''
    cost = 0.0
    isExpense = True

    if len(input) < 3:
        error_handler.ERROR_FEW_ARGS()
    


def display():
    '''
    transaction_list = load_transactions()

    for transaction in transaction_list:
        print(transaction)
    '''

    read_transactions_from_file()

def quit():

    print("Goodbye!")

## Save and Load Transactions

def write_transaction_to_file(transaction):
    file = open('transaction_history.txt', 'a+')

    file.write(transaction)

    file.close()

def read_transactions_from_file():
    file = open('transaction_history.txt', 'r')

    if file.mode == 'r':
        contents = file.read()
        print(contents)