import datetime
import helper

class Transaction:

    def __init__(self, id, name = '', cost = 0.0, isexpense = True):
        self.id = id
        self.name = name
        self.cost = cost
        self.isexpense = isexpense
        self.date = datetime.datetime.now()

    def __repr__(self):
        return 'name: {0}\ncost: ${1}\nisExpense: {2}\ndate: {3} \n'.format(self.name, self.cost, self.isexpense, helper.pretty_time_format(self.date));

    def quick_display(self):
        return '{0}\t{1}\t{2}\t{3}\n'.format(self.id, self.name, helper.pretty_time_format(self.date), self.cost)