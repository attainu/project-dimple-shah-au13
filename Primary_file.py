from restaurant_data import *
from Tasks import *
import argparse


class MainPage:
    def __init__(self):
        self.List_foods = []
        self.List_drinks = []
        self.List_services = []
        self.List_disc = []

    def details(self, a):
        print(a)
        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")
        i = 0
        while i < len(self.List_foods) or i < len(self.List_drinks):
            var_space = 1
            if i <= 8:                   # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                var_space = 2
            if i < len(self.List_foods):
                food = " (" + str(i + 1) + ")" + " " * var_space + str(self.List_foods[i]) + "  | "  # Styling out the index number for the food or item and starting out from 1 for better human readability
            else:
                food = " " * 36 + "| "  # 36 is a constant for indention in console to fixup List in print
            if i < len(self.List_drinks):
                drink = "(" + str(41 + i) + ")" + " " + str(self.List_drinks[i]) 
            else:
                drink = ""
            print(food, drink)
            i += 1
        print("*" * 29 + "OTHER SERVICES" + "*" * 29)
        print(" |NO| |SERVICE NAME|      |PRICE|")  # Services Menu Structure

        i = 0
        while i < len(self.List_services):
            print(" (" + str(81 + i) + ")" + " " + str(self.List_services[i]))   # Services starts from 81 + and now it is being enumarated into a List.

            i += 1
        print("=====================================")
        pr = self.List_disc[:3]
        for i in range(len(self.List_disc)):
            if i > 2:
                print("Order your food and get", float(self.List_disc[i]) * 100, " % Off with Min. order Rs", pr[0])
                pr.pop(0)
        print("\n")
        print("If you would to check with this Restaurant? just enter")
        print("You wish to check with the prices on other Restauran? say yes!")
        take = input()
        if take:
            self.List_restaurant()
        s = Food(self.List_foods, self.List_drinks, self.List_services, self.List_disc, a)
        s.def_main()

    def List_of_foods_drinks(self):
        l = {"1": "Sahara_Star", "2": "Hilton", "3": "J.W.Marriott", "4": "Oberoi"}
        print("*" * 5 + "( If you wish to know the price of the food which you are looking for,\nplease enter the food and drink name )" + "*" * 5)
        print("\n")
        print("If you wish to go through the restaurant names and order your food, just enter")
        print("\n")
        new_food = input("Please enter food name: ") 
        new_drink = input("Please enter drink name: ")
        if new_food == "" and new_drink == "":
            self.List_restaurant()
        else:
            low_high_food = {}  # creating dictionary to store the food and price
            low_high_drink = {}  # creating dictionary to store the drink and price
            for key, val in l.items():
                a = Catalogue_(key)  # creating instance of Catalogue_ to fetch data from database
                item1, item2 = a.food_name_wise1(new_food, new_drink)
                if len(item1) == 0:
                    item1 = "Not found"
                if len(item2) == 0:
                    item2 = "Not found"
                low_high_food.update({val: item1})  # updating food and rink prices to dictionary
                low_high_drink.update({val: item2})
            print()
            print("*" * 10 + "FOOD" + "*" * 10)
            for k, v in low_high_food.items():
                print(k, "    :   ", v)
            print("*" * 10 + "DRINKS" + "*" * 10)
            for k2, v2 in low_high_drink.items():
                print(k2, "    :   ", v2)
            print("* " * 25)
            print("\n")
            print("If you wish to check with other food..please say yes!")
            print("If you wish to order this food, just enter")
            print()
            print("* " * 25)
            input__ = input("yes or no")
            if input__ != "":
                self.List_of_foods_drinks()
            else:
                self.List_restaurant()

    def complete_information(self):                           # To fetch the food and drink based on RESTAURANT name.
        l = {"1": "Sahara_Star", "2": "Hilton", "3": "J.W.Marriott", "4": "Oberoi"}
        name_res = input("Please select the RESTAURANT..: ")

        if len(name_res) == 1:
            a = Catalogue_(name_res)
            self.List_foods, self.List_drinks, self.List_services, self.List_disc = a.def_full_file_reader()
            self.details(l[name_res])
        else:
            print("Please enter the valid input")
            self.complete_information()

    def List_restaurant(self):
        print("You can go through the Restaurant Names and choose one!!")
        print("\n")
        print("*" * 31 + "RESTAURANT NAMES" + "*" * 32 + "\n\t(1) Sahara_Star\n\t(2) Hilton\n\t(3) J.W.Marriott\n\t(4) Oberoi\n" + "_" * 72)
        print("=====================================")
        self.complete_information()

    def main_page(self):
        print("\n\n\n")
        print("* " * 15 + "Welcome " + "* " * 20)
        print("\n")
        print("* " * 10 + "Choose and Taste to your Place !!!" + "* " * 13)
        print("\n")
        print("*" * 48)
        print("\n")
        print("Hotels to Celebrate Life !!!")
        print(" " * 10 + "We are ready to serve !!!" + " " * 20)
        print("\n")
        print("*" * 48)
        print("\n")
        print("\n")
        self.List_of_foods_drinks()

    def update_menu(self, args):
        d_update = Catalogue_(args.resName[0])
        foodToUpdate = input("enter food name and price to be updated")
        d_update.update_food(foodToUpdate)
        drinkToUpdate = input("enter drink name and price to be updated")
        d_update.update_drink(drinkToUpdate)
        print("updated")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = '''==================================Update food and drinks into menu==================================''') 
    parser.add_argument("--resName", type = str, nargs = 1, 
                        metavar = "rs_name", default = None, 
                        help = "RESTAURANT NAMES" + "\n"     

                        
                        "\t(1) Sahara_Star\n"                              
                        "\t(2) Hilton\n"
                        "\t(3) J.W.Marriott\n"
                        "\t(4) Oberoi\n")  # defining arguments for parser object 
    args = parser.parse_args()

    mP = MainPage()
    if args.resName != None:
        mP.update_menu(args)
    else:
        mP.main_page()  # python 
#Primary_file.py
#Displaying Primary_file.py.