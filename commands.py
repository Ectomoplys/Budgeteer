import error_handler
import datetime
from database import Database
import helper

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
    database = Database()

    if commands[0] == 'price':
        if commands[1] == 'greater':
            database.find_greater(commands[2])
        elif commands[1] == 'less':
            database.find_less(commands[2])

    elif commands[0] == 'isexpense':
        database.find_isexpense( True if (commands[1] == 'yes' or commands[1] == 'y') else False)
    elif commands[0] == 'date':
        database.find_date(commands[1])
    elif commands[0].isalnum():
        database.find_name(commands[0])
    return

def add(input):

    if len(input) < 3:
        error_handler.ERROR_FEW_ARGS()
        return

    if len(input) > 3:
        error_handler.ERROR_MANY_ARGS()
        return

    _name = input[0]
    _cost = float(input[1])
    _isExpense = True if (input[2] == 'y' or input[2] == 'yes') else False
    
    database = Database()

    _id = database.resolve_id()

    _date = datetime.datetime.now()
    _day = _date.day
    _month = _date.month
    _year = _date.year
    

    transaction = {
        'name' : _name,
        'cost' : _cost,
        'isexpense' : _isExpense,
        'date' : {
                    'day' : _day, 
                    'month' : _month, 
                    'year' : _year,
                },
        'id' : _id,
    }

    database.add_transaction(transaction)
    
def delete(id):
    database = Database()
    database.delete_transaction(id)

def display(commands = None):

    database = Database()
    database.display_transactions()

def clear():
    confirmation = input('Are you sure? This will delete all records! ')

    if confirmation == 'yes':
        database = Database ()
        database.clear_transactions()

def quit():
    print("Goodbye!")

def test():
    return 
