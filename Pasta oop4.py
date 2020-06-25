'''Oop based system that organizes differnts restaurants , the system dont utilizes none system of degubing it means
that is very easy to break the whole system ... The main concept where is to work the OOP and the main things that compose
it'''

class menu:
    # Constructor
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def get_time(self):
        # get the time and config it
        if self.start_time or self.end_time < 12:
            self.end_time = str(self.end_time) + 'AM'
            self.start_time = str(self.start_time) + 'AM'
        elif self.start_time > 12:
            self.start_time = str(self.start_time) + 'PM'
        elif self.end_time > 12:
            self.end_time = str(self.end_time) + 'PM'
        return self.start_time and self.end_time

    def __repr__(self):
        # print the menu
        self.get_time()
        return " {} menu is available from {} to {}".format(self.name, self.start_time, self.end_time)



    def calculate_bill(self, purchased_items):

        # calculate the bill using list comprehension  :)
        price_lst = list()
        price = list()
        self.purchased_items = purchased_items
        for k in self.purchased_items:
            for v in self.items:
                if k == v:
                    price_lst.append(self.items[k])

        sum_list = sum(price_lst)
        print(sum_list)

class flagship_store(menu):
    #Store number1
    def __init__(self):
        self.address = "1232 West End Road"
        self.menus = ["early_bird" ,"dinner" ,"brunch" ,"kids"]

    def available_menus(self, time):
        self.time = time
        # show all the menus based what input its given

        if self.time == 3 and 4:
            self.final_meal = self.menus[1]
        elif self.time == 5 and 6:
            self.final_meal = self.menus[0:1]
        elif 7 <= self.time <= 10:
            self.final_meal = self.menus[1]
        elif self.time == 11:
            self.final_meal = self.menus[0:3]
        elif 12 <= self.time <= 16:
            self.final_meal = self.menus[1:3]
        elif 17 <= self.time <= 21:
            self.final_meal = self.menus[3]

        print(self.final_meal)


    def __repr__(self):
        return "1232 West End Road"

#------------------------------------------------------
class new_installment(menu):
    # Store Number 2 Have the same menu
    #if 10000 <= number <= 30000: pass >>> Logic that i learned for chose which menu
    def __init__(self):

        self.address = "12 East Mulberry Street"
        self.menus = ["early_bird" ,"dinner" ,"brunch" ,"kids"]

    def available_menus(self , time ):
        self.time = time
        #show all the menus based in time

        if self.time == 3 and 4:
            self.final_meal = self.menus[1]
        elif self.time == 5 and 6:
            self.final_meal = self.menus[0:1]
        elif 7 <= self.time <= 10 :
            self.final_meal = self.menus[1]
        elif self.time == 11:
            self.final_meal = self.menus[0:3]
        elif 12 <= self.time <=16:
            self.final_meal = self.menus[1:3]
        elif 17 <= self.time <= 21:
            self.final_meal = self.menus[3]

        print(self.final_meal)

    def __repr__(self):
        return "12 East Mulberry Street"

#-Arepas one restaurant that utilizes the logic from the Menu class but have only one menu
class arepas_place:
    # arepas franchise
    def __init__(self):

        self.address = "12 East Mulberry Street"
        self.menus = ["Take a arepa"]

    def available_menus(self , time ):
        self.time = time
        #show all the menus based in time

        if 10 <= self.time <= 20:

            print(self.menus[0])

    def __repr__(self):
        return "12 East Mulberry Street"

class business:
    def __init__(self ,name ,franchise):
        self.name = name
        self.franchise = franchise


#Menus for the all the franchises it also contains the hours that u can ask for any menu
brunch = menu("brunch", {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = menu("early_bird", {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 3, 6)

dinner = menu("dinner", {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 5, 11)

kids = menu("kids", {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)
 #menu that is connect to arepa franchise
arepas_menu = menu("Take a’ Arepa" ,{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},10 ,20 )

bssn1 = business("Basta Fazoolin' with my Heart" , [flagship_store , new_installment , arepas_place])

print("Show the power of the dunder __repr__")
print(brunch , "\n")
print(early_bird , "\n")
print(dinner, "\n")


print("Show the class flag_ship logic to choose if a menu if avaliable or not based in input " , "\n")
new_st = new_installment()
new_st.available_menus(13)
new_st.available_menus(11)
