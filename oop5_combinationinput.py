'''Simple code that aims to train OOP , and the ideia is that the code can recive inputs and check if they are good inputs
after that the code will use all possible combinations for a imput '''

magic_error = 'B00BX5'
from itertools import combinations

class tree_n():

    def __init__(self):
        self.items = []
        pass

    def check_inp(self , inp): #check that all input are ints
        try :
            if type(inp) == int:
                return inp
        except magic_error:
            print("Not a good number try again")



    def add(self, item): # Add input of numbers to the the calc
        self.a  = self.check_inp(item)

        self.items.append(self.a)


    def pri_it(self): # Print all numbers already have been add to the calc
        for i in self.items:
            print(i)

    def all_comb(self): # Print all possible combinations

        self.output = sum([list(map(list, combinations(self.items, i))) for i in range(len(self.items) + 1)], [])
        print(self.output)



ab = tree_n()
ab.add(4)
ab.add(5)
ab.add(3)
ab.pri_it()
ab.all_comb()