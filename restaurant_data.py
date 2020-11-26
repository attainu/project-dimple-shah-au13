class Catalogue_:                                    # class to fetch the restaurant menu

    # Initialise variables to fetch food,drink and services from database
    def __init__(self, n):
        self.List_foods = []                          # to fetch List of foods
        self.List_drinks = []                         # To fetch List of drinks
        self.List_services = []                       # To fetch services
        self.var_Discount_ = []                     # First Discount starts.
        if n == str(1):
            self.name = "Sahara_Star"                   # file name to fetch the details
        if n == str(2):
            self.name = "Hilton"                         # file name to fetch the details
        if n == str(3):
            self.name = "J.W.Marriott"                     # file name to fetch the details
        if n == str(4):
            self.name = "Oberoi"                       # file name to fetch the details

    def def_full_file_reader(self):
        file_foods = open('Catalogue_file' + "\\" + self.name +
                          "\\" + 'List_foods.fsd', 'r')  # Reading Food List
        for i in file_foods:  # Line by line reading
            # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
            self.List_foods.append(str(i.strip()))
        file_foods.close()

        file_drinks = open('Catalogue_file' + "\\" + self.name +
                           "\\" + 'List_drinks.fsd', 'r')  # Reading Drinks List
        for i in file_drinks:
            self.List_drinks.append(str(i.strip()))
        file_drinks.close()

        file_services = open('Catalogue_file' + "\\" + self.name +
                             "\\" + 'List_services.fsd', 'r')  # Reading Services
        for i in file_services:
            self.List_services.append(str(i.strip()))
        file_services.close()

        file_Discounts = open('Catalogue_file' + "\\" +
                              self.name + "\\" + 'Disc.fsd', 'r')
        for i in file_Discounts:
            self.var_Discount_.append(i)
        file_Discounts.close()

        i = 0
        while i <= (len(self.List_foods) - 1):   # Enumarte through food List to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
            if 'Rs' in self.List_foods[i]:
                self.List_foods[i] = str(self.List_foods[i][:self.List_foods[i].index('Rs') - 1]) + ' ' * (20 - (
                    self.List_foods[i].index('Rs') - 1)) + str(self.List_foods[i][self.List_foods[i].index('Rs'):])
            i += 1

        i = 0
        while i <= (len(self.List_drinks) - 1):
            if 'Rs' in self.List_drinks[i]:
                self.List_drinks[i] = str(self.List_drinks[i][:self.List_drinks[i].index('Rs') - 1]) + ' ' * (20 - (
                    self.List_drinks[i].index('Rs') - 1)) + str(self.List_drinks[i][self.List_drinks[i].index('Rs'):])
            i += 1

        i = 0
        while i <= (len(self.List_services) - 1):
            if 'Rs' in self.List_services[i]:
                self.List_services[i] = str(self.List_services[i][:self.List_services[i].index('Rs') - 1]) + ' ' * (20 - (
                    self.List_services[i].index('Rs') - 1)) + str(self.List_services[i][self.List_services[i].index('Rs'):])
            i += 1
        return (self.List_foods, self.List_drinks, self.List_services, self.var_Discount_)

    def food_name_wise1(self, foo_name="", drink_name=""):
        file_foods = open('Catalogue_file' + "\\" + self.name +
                          "\\" + 'List_foods.fsd', 'r')  # Reading Food List
        for i in file_foods:
            if foo_name in i:  # Line by line reading
                # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
                self.List_foods.append(str(i.strip()))
        file_foods.close()
        file_drinks = open('Catalogue_file' + "\\" + self.name +
                           "\\" + 'List_drinks.fsd', 'r')  # Reading Drinks List
        for i in file_drinks:
            if drink_name in i:
                self.List_drinks.append(str(i.strip()))
        file_drinks.close()
        i = 0
        while i <= (len(self.List_foods) - 1):  # Enumarte through food List to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
            if 'Rs' in self.List_foods[i]:
                self.List_foods[i] = str(self.List_foods[i][:self.List_foods[i].index('Rs') - 1]) + ' ' * (20 - (
                    self.List_foods[i].index('Rs') - 1)) + str(self.List_foods[i][self.List_foods[i].index('Rs'):])
            i += 1
        i = 0
        while i <= (len(self.List_drinks) - 1):
            if 'Rs' in self.List_drinks[i]:
                self.List_drinks[i] = str(self.List_drinks[i][:self.List_drinks[i].index('Rs') - 1]) + ' ' * (20 - (
                    self.List_drinks[i].index('Rs') - 1)) + str(self.List_drinks[i][self.List_drinks[i].index('Rs'):])
            i += 1
        return (self.List_foods, self.List_drinks)

    def update_food(self, add_food):
        with open('Catalogue_file' + "\\" + self.name + "\\" + 'List_foods.fsd', 'a') as file_foods:  # Reading Food
            file_foods.write("\n")
            file_foods.write(add_food)

    def update_drink(self, add_drink):
        with open('Catalogue_file' + "\\" + self.name + "\\" + 'List_drinks.fsd', 'a') as file_drinks:  # Reading Drinks List
            file_drinks.write("\n")
            file_drinks.write(add_drink)
#restaurant_data.py
#Displaying restaurant_data.py.