import datetime
import prettyformat as pretty


class Transaction:

    def __init__(self):
        self.name = ''
        self.cost = 0.00
        self.isexpense = False
        self.date = datetime.datetime.now()
        self.id = 0

    def __init__(self, name, cost, isexpense):
        self.name = name
        self.cost = cost
        self.isexpense = isexpense
        self.date = datetime.datetime.now()

    def __str__(self):
        return 'name: {0}\ncost: {1}\nisExpense: {2}\ndate: {3} \n'.format(self.name, self.cost, self.isexpense, pretty.time_format(self.date));
