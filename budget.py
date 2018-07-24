#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from database import Database
from parser import Parser

def main():
    Parser()
    
    starting = True

    '''while starting:
        os.system('clear')

        query = input("command>> ")
        queries = query.split(" ")

        if queries[0] == 'test':
            database = Database('test_database')
        else:
            database = Database('budget_database')

        # starting = parser.new_parser(database, queries)
    '''

main()


