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
    def __init__(self, name, items, start_time, end_time):
        super().__init__(self, name, items, start_time, end_time)
        self.address = "1232 West End Road"
        self.menus = ["early_bird" ,"dinner" ,"brunch" ,"kids"]

    def __repr__(self):
        print("1232 West End Road")

#------------------------------------------------------
class new_installment(menu):
    # Store Number 2
    def __init__(self):

        self.address = "12 East Mulberry Street"
        self.menus = ["early_bird" ,"dinner" ,"brunch" ,"kids"]

    def available_menus(self , time):
        self.time = time
        self.time = int(self.time)




    def __repr__(self):

        print("12 East Mulberry Street")



#------------------------------------------------------
#Menus

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



ab = new_installment()
ab.available_menus(4)