from transaction import Transaction
import pickle
import error_handler

def help():

    print("HELP")
    print('''
            ARGUMENT                    RETURN TYPE     FUNCTION
help                                    -> string       displays help
add         [name] [cost] [isExpense]   -> bool         adds a new expense, returns True is success
delete      [id]                        -> void         deletes a transaction
find        [name|cost|isExpense|date]  -> Transaction  searches for a transaction
display                                 -> string       displays all transactions
            [date]                      -> string       displays list of transactions for certain date
            sort [date|cost]            -> string       displays list of transactions sorted by [argument] from low to high
quit                                    -> void         quits program
    ''')

def find(commands):
    return


def add(input):
    name = ''
    cost = 0.0
    isExpense = True

    if len(input) < 3:
        error_handler.ERROR_FEW_ARGS()
        return

    if len(input) > 3:
        error_handler.ERROR_MANY_ARGS()
        return

    name = input[0]
    cost = float(input[1])
    isExpense = True if (input[2] == 'y' or input[2] == 'yes') else False

    transaction = Transaction(name, cost, isExpense)

    save_transation(transaction)

def display():
    print('''
ID              NAME    COST    DATE
    ''')

    transaction_list = load_transactions()

    for transaction in transaction_list:
        print(transaction)

def quit():

    print("Goodbye!")

## Save and load Transactions to TEXT file

def save_transation(transaction):
    file = open('transactions.pkl', 'ab')

    pickle.dump(transaction, file)

    file.close()

def load_transactions():
    transaction_list = []

    file = open('transactions.pkl', 'rb')

    while 1:
        try:
            transaction = pickle.load(file)
        except EOFError:
            break

        transaction_list.append(transaction)

    return transaction_list




