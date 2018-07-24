from pymongo import MongoClient
from mongoengine import connect
import datetime

class Database(object):

    def __init__(self, database = 'budget_database'):
        self.client = MongoClient()
        self.database = self.client[database]
        self.collection = self.database['transactions']
        connect('budget_database')

    def add_transaction(self, transaction):

        result = self.collection.insert_one(transaction)
        print('Transaction added: {0}'.format(result.inserted_id))

    def display_transactions(self):
        cursor = self.collection.find()

        for found in self.collection.find():
            print(found)

    def delete_transaction(self, id):
        print('Deleting Transaction with id {0}'.format(id))
        self.collection.delete_one( { 'id' : int(id)} )

    def clear_transactions(self):
        self.collection.remove( {} )

    def find_transaction(self, ):
        self.collection.find( {})

    def size(self):
        return self.collection.count()
    
    def resolve_id(self):
        _id = self.collection.count()

        while self.collection.find( { 'id' : _id } ).count() > 0:
            _id *= 2
        
        return _id

    def find_greater(self, price):
        print('searching for transaction greater than {0}'.format(float(price)))

        for found in self.collection.find( { "cost" : { "$gt" : float(price) } } ):
            print(found)

    def find_less(self, price):
        print('searching for transaction less than {0}'.format(float(price)))

        for found in self.collection.find( { 'cost' : { '$lt' : float(price) } } ):
            print(found)

    def find_isexpense(self, isexpense):
        for found in self.collection.find( { 'isexpense' : isexpense } ):
            print(found)
    
    def find_date(self, date):
        _day = datetime.datetime.now()
        _month = datetime.datetime.now()

        if len(date) == 2:
            _month = int(date)

            for found in self.collection.find( { 'date.month' : _month } ):
                print(found)

        elif len(date) == 4:
            _year = int(date)

            for found in self.collection.find( { 'date.year' : _year } ):
                print(found)

        elif len(date) == 5:
            _date = date.split('/')
            
            _month = int(_date[0])
            _day = int(_date[1])

            for found in self.collection.find( {
                                                    'date.month' : _month,
                                                    'date.day' : _day,
                                                } ):
                print(found)


        elif len(date) == 7:
            _date = date.split('/')
            _month = int(_date[0])
            _year = int(_date[1])

            for found in self.collection.find( {
                                                    'date.month' : _month,
                                                    'date.year' : _year,
                                                } ):
                print(found)

    def find_name(self, name):
        for found in self.collection.find( { 'name' : name } ):
            print(found)