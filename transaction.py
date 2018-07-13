import datetime
import helper

class Transaction(object):

    def __init__(self, name = '', cost = 0.0, isexpense = True):
        self.name = name
        self.cost = cost
        self.isexpense = isexpense
        self.date = datetime.datetime.now()

    def __repr__(self):
        return '{0}\t{1}\t{2}\t{3}\n'.format(id(self), self.name, self.cost, helper.pretty_time_format_quick(self.date))

    def quick_display(self):
        return '{0}\t{1}\t{2}\t{3}\n'.format(id(self), self.name, self.cost, helper.pretty_time_format_quick(self.date))