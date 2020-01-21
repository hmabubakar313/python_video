# import converters
#  changing var type
# name = input("What is your name? ")
# color = input("what color do you like? ")
# print("my name is "+name + " i like"+color)
# weight = input("Enter your weight(pounds) please! ")
# kg = int(weight) * 2.2
# # float(kg)
# print(kg)
# x = 5
# x += 3
# print(x)
# methods of python
# name = "My name is Muhammad Abu Bakar"
# # x = name.lower()
# x = name.find("Abu Bakar")
# print(x)
# print("Muhammad" in name)
# print(name)
# if else conditions
# price = 100
# good_credit = False
# not_good = False
# if good_credit:
#     down_payment = 0.1 * price
#     print(f"downpayment for good credit : ${ down_payment}")
# elif not_good:
#     down_payment = 0.2 * price
#     print(f"downpayment for good credit : ${ down_payment}")
# else:
#     print("else statement")

# * logical operators
# study = True
# hard_work = True
# if (study and hard_work):
#     print("you have bright future")
# study = True
# hard_work = False
# if (study and not hard_work):
#     print("you have bright future")
# study = True
# hard_work = False
# if (study or hard_work):
#     print("you have bright future")
# study = False
# hard_work = True
# if (study and hard_work):
#     print("you have bright future")

# ?example for logical operators
# name = input("Enter your name Please! ")
# check_length = len(name)
# if (check_length < 3):
#     print("Plese enter a name more than 3 lettwers")
# elif (check_length > 50):
#     print("please enter name less than 50 char ")
# else:
#     print("Success")


# ? weight converter
# w = int(input("please enter your weight? "))
# unit = input("please selest unit of the weight pounds(l) or killo(k)")
# if unit.lower() == "p":
#     net_weight = w * 0.45
#     print(f"your net weight is : {net_weight}")
# else:
#     net = w / 0.45
#     print(f"your net weight is : {net} ")

# ! guessing a number game in whhile loop

# a = 5
# i = 1
# while (i <= 3):
#     guess = int(input("Enter the correct number"))
#     i = i+1
#     if (a == guess):
#         print("you won")
#         break

# !simple while loop game
# command = ""
# while (command != quit):
#     command = input("> ").lower()
#     if (command == "start"):
#         print(">car started..")
#     elif (command == "stop"):
#         print("car stopped")
#     elif (command == "help"):
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quite - to quite the game
#         """)

# ?list programme
# numbers = [34, 2, 3, 4, 5]
# numbers.clear()
# print(numbers)
# numbers.sort()
# print(numbers)

# removing list

# mapping

# phone = input("enter your phone number ")
# digits_mapping = {
#     "1": "one",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"

# }
# result = ""
# for x in phone:
#     result += digits_mapping.get(x, "!") + " "
# print(result)

# ? setting up emojis

# messege = input(">")
# words = messege.split(" ")
# emojis = {
#     ":)": "🥰",
#     "):": "😪"
# }
# output = " "
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
# def ana():
#     print("Hello there")
#     print("Have a Good Day")


# print("start")
# ana()
# print("End here")

# exception handling
# try:
#     x=int(input("ENter your age"))
# except ZeroDivisionError:


# !classes in python
# class Person:
#     def __init__(self, x, y):
#         # self.x = x
#         # self.y = y
#         self.x = x
#         self.y = y

#     def name(self):
#         print("My name is Ali")

#     def talk(self):
#         print("his way of talking is so good")


# person1 = Person()
# person1.name()
# person2 = Person()
# person2.talk()
# person = Person(20, "Abu Bakar")
# print(person.x, person.y)

# !inheritance
# class Human:
#     def walk(self):
#         print("the can walk")


# class Boy(Human):
#     pass


# class Girl(Human):
#     pass


# peron1 = Girl()
# peron1.walk()

# ? using converters module
# print(converters.kg_to_lbs(30))

# !making new directory and new module inside it
# import ecommerce.shipping
# ecommerce.shipping.calculate_shipping()

# !using from statement for the package
# from ecommerce.shipping import calculate_shipping
# calculate_shipping()
# calculate_shipping()

# ?generate randoom numbeer
# import random
# for i in range(4):
#     print(random.randint(0, 10))

# members = ["Abu Bakar", "Ali", "Asif", "Umair", "Anas"]
# leader = random.choice(members)
# print(leader)

# ! pathlib library
# from pathlib import Path
# path = Path()
# for files in path.glob("*"):
#     print(files)

# ! working with xl file
# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
# wb = xl.load_workbook("transactions.xlsx")
# sheet = wb["Sheet1"]
# cell = sheet["a1"]
# cell = sheet.cell(1, 1)
# print(sheet.max_row)
# for row in range(2, sheet.max_row + 1):
#     cell = sheet.cell(row, 3)
#     net_value = cell.value*0.9
#     net_value_cell = sheet.cell(row, 4)  # giving value to the cell
#     net_value_cell.value = net_value

# x = Reference(sheet, min_row=2, max_row=sheet.max_row+1, min_col=4, max_col=4)
# chart = BarChart()
# chart.add_data(x)
# sheet.add_chart(chart, "e2")
# wb.save("transactionls.xlsx")
