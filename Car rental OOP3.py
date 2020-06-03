from datetime import datetime

class rento:

    def __init__(self):
        self.cust = 'cust'
        self.cust = list()
        self.card = 'card'
        self.card = {1: 'Ford 1992', 2: 'Mustang 2012', 3: 'Honda Civic', 4: 'Kia', 5: 'Mazda 3'}
        self.rentt = 'rentt'
        self.rentt = dict()
        self.current = 'current'
        self.current = dict()

    def showcars(self):
        #let the customer see numbers of cars
        return print(self.card.values())

    def customer(self):
        #create a profile to the customer
        acus = input('Customer name:')
        self.cust.append(acus)

    def rentsel(self):
        #select the car and update de dic
        print(self.card)
        carsel = input('Please select a car that you would like to rent:')
        carsel = int(carsel)# Select which car
        try:
            #Check if the car was already rented
            for (key, value) in set(self.card.items()) & set(self.rentt.items()):
                print('%s Is allready rented ' % (value))
                return
        except:
            print("All cars are in the garage and can be used")

        dicsel = self.card.get(carsel)
        self.rentt.update({carsel: dicsel})# Add the rented car
        print('\n')
        print(self.cust)
        cussel = input('Please select the costumer:') #Select customer
        cussel = int(cussel)
        cusfn = self.cust[cussel]

        nmdays = input('Please inputs number of days it will rent:')
        nmdays = int(nmdays)
        print('The car was rented for ' , nmdays , 'days and the car rented was' , self.rentt.values(), 'by the customer ', self.cust)

        #genarate the ticket
        self.totalpay = nmdays * 60.30
        self.current.update({cusfn : self.totalpay})

    def closet(self):

        for i in self.current.keys():
            print('Please select one of the of the following customers to riceive the bill' ,'\n' , i)
        chs = input('Select:')
        print('The total is ', self.current[chs])
        #return print('You must pay' , self.totalpay, 'you started to use ours services' ,  self.today  )



openit = rento()
while True:
    print("1) Show all cars" , '\n' , "2)Create a New customer" , '\n' , "3)Select a car and rent it" , '\n' , "4)Close the count ")
    chs1 = input('Please select what would you want to do do:')
    chs1 = int(chs1)
    try:
        if chs1 == 1: openit.showcars()
        elif chs1 == 2 : openit.customer()
        elif chs1 == 3 : openit.rentsel()
        elif chs1 == 4 : openit.closet()
        else :
            print("Not a good input")
    except:
        print("It has been a problem try open it again")