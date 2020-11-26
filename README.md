**********************************************PYTHON PROJECT : SWIGGY*******************************************************************

****************************************************************************************************************************************

******Introduction: Food Ordering System******

Ever felt lazy to dine out at any restaurant? FOS helps its users tuck in their desired appetite.
The FOS allows its users to order food from available restaurants by providing discounts.
Fussy eaters can search with the desired food item, instead of looking over the entire menu.
The ordering is limited to only one restaurant at a time and the bill would be inclusive of the item names and the quantity ordered.

*******************************************************************************************************************************************

******Problem statement:******

Design a food ordering system, so that customer should be able to place an order by giving items or restaurant names. Customer can select available restaurants which offers the lowest price for that order item. Should be able to keep track of all items served by each restaurant.

*******************************************************************************************************************************************

************DOWNLOAD*************

Download the file from the following URL...
https://github.com/attainu/project-dimple-shah-au13.git

(Click on the "clone or download" button on your left  --download ZIP)

*******************************************************************************************************************************************


*********Method Used**********

• OOPS Concept.

*******************************************************************************************************************************************

***************IMPORTING MODULES***************

import os
import smtplib                                                                         #for emailing
import datetime
import argparse

*******************************************************************************************************************************************

******Approach and Implementation******:

*** Below listed libraries were imported  ==>

• Import DATETIME - Module for getting the Modification Timestamp

• argparse- Used to get command line arguments into our program

• Initially, a List (restaurant) of dictionaries was used with “menu” as key and “values” as prices.

• A DB Folder(restaurant_data.py) was created which comprises of sub folders, which holds individual restaurant data in .fsd\* format.

• Details to perform the tasks “Order, report generation, payment”, were saved in individual .py file (Tasks.py)

• File handling was adopted to fetch the data from the resto_data.py (DB Folder) cause when the input of “food and drink” was given on the terminal, Restaurant information will be fetched from this file.

• System can update new food or drink name into the restaurants menu using CLI arguments.

• In a Main function, the operations and data files, restaurant_data.py and Tasks.py were imported to perform specific tasks as per the end user need.

• When compiled, customer can search the food name, then the specific item would be displayed from all available restaurants with price inclusive.

• The next available option would be to either proceed with the current order or to decline and look over the menu available. If “order food” was chosen, the system will fetch the food, drinks, service, and discount details from the file. (by creating instance of a class Database\_ and calling the function def_full_file_reader()) once the food item was chosen, the system would throw the question to choose the quantity.

• Payment can be made by selecting an appropriate option on the terminal. (The system will redirect customer into the bill, by calling the function def_payment ()) Upon clicking the option to make a payment, the bill will be generated and uploaded into a report file. (def_report () function will be called and update the bill into the report. fsd file) No further item requests until items which are in the processing are completed (a time delay was created using time module)

• Multiple items can be placed from one restaurant at a time, the maximum quantity to order is 80. Each restaurant has a maximum processing capacity of items at any given time. A list was used to store the number of orders, the system will prompt the customer, whether they need to exit or would like to go with another order.

*******************************************************************************************************************************************

*****Future Scope******:

• The order confirmation update can be sent to the customer’s email.
• Multiple payment methods can be included for the ease of the customer.

*******************************************************************************************************************************************