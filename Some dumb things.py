"""
#Oh yes, the guest list
guest_list = ['Alice', 'Bob', 'Charlie', 'David']
guest_list.sort(reverse=True)
print(guest_list)

#Uh, dont bother ask me
from tkinter import ACTIVE, NO


gpu = ["4080 super", "5090", "1660 super", "5080"]
gpu.reverse()
print(gpu)
#Somedumb project about agents
valorant_agents = [
    "Brimstone",
    "Viper",
    "Omen",
    "Killjoy",
    "Cypher",
    "Sova",
    "Sage",
    "Phoenix",
    "Jett",
    "Reyna",
    "Raze",
    "Breach",
    "Skye",
    "Yoru",
    "Astra",
    "KAY/O",
    "Chamber",
    "Neon",
    "Fade",
    "Harbor",
    "Gekko",
    "Deadlock",
    "Iso",
    "Clove"
]

valorant_agents.sort()
for agent in valorant_agents:
    print(f"{agent.upper()}, you are suck!")

my_favoite_agents= valorant_agents[:]
my_bf_favourite_agents = valorant_agents[:]

my_favoite_agents=my_bf_favourite_agents

my_favoite_agents.append("Waylay")

print("This is your favourite agents list:", my_favoite_agents)
print("\nThis is your boyfriend favourite agents list:", my_bf_favourite_agents)
#And the simple, yet elegant alien colors
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
        print("You just earned 5 points")
else :
        print("\n")
#Still username
user_names=[]
for user_name in user_names:
    if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
    else:
            print("We need to find some users!")
print("\nThat's it!")
#For usersname
current_users = [' Alice', 'David', 'Homie','Belle']
new_users=['Admin', 'Miyabi', 'Belle']
#For casesensitive
current_lower_users = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_lower_users:
        print(f"Sorry, {new_user} have already been taken")
    else:
        print(f"Good, the name {new_user} is available")
#For number from ordinal
ordinal_numbers= list(range(1,10))
for ordinal_number in ordinal_numbers:
    if ordinal_numbers == 1:
                print("1st")
    elif ordinal_number == 2:
                print("2nd")
    elif ordinal_number == 3:
                print("3rd")
    else: 
        print(f"{ordinal_number}th\n")
#Person
person = {'first_name': 'Vu Minh', 'last_name':'Long','age': '18','city': 'Ha Noi'}
for k,v in person.items():
        print(f"Key:{k}")
        print(f"Value: {v}\n")
#People
myhomie= {'FirstName':'Pham Phu', 'LastName' :'Thai', 'Address': 'Ha Noi', 'Age':'18'}
mybrother ={'FirstName': 'Nguyen Trung', 'LastName': 'Kien', 'Address':'Ha Noi', 'Age':'14'}
Allfamiliars= [myhomie, mybrother]
for person in Allfamiliars:
    print(f"Welcome {person['FirstName']} {person['LastName']}, You are now {person['Age']} and live in {person['Address']}")
#FavouritePlaces
favourite_places = {'Long': ['Japan', 'VietNam', 'Korea'], 'Thai': ['VietNam', 'USA', 'Peru']}
for name, places in favourite_places.items():
        print(f"{name}'s favourite places is:")
        for countries in places:
            print("\t", countries)
            

#RentalCars
v=input("Tell me what kind of car you like: ")
print(f"Oh, so you like", v.title(), "huh?")
#RestaurantSeating
people= input("How many people are there in your group? ")
if int(people)>8:
            print("Sorry, you have to wait for a table")
else:
    print("You are welcome")
#multiples of Ten
number= int(input("Tell me a number: "))
if number%10 ==0:
        print("This number is a multiple of 10")
else:
        print("This number is not a multiple of 10")

#Pizza Toppings
prompt = "\nWhat toppings do you want on your pizza? "
prompt +="\nEnter 'quit' to quit "

while True:
    mess=input(prompt)
    if mess == 'quit':
        break
    else:
        print(f"Kay, i will add {mess.title()} to your pizza!")

#Movie Ticket
prompt= ("\nTell me your age and I will tell you the price! ")
prompt +=("Type 'quit' to exit! ")

while True:
    mess= input(prompt)
    if mess == 'quit':
        break
    age = int(mess)
    if age <=3:
        print(f"\nFor this {mess}, your price is free!")
    elif age<=12:
        print(f"Oh, your age is {mess} so your price is 10$")
    else:
        print(f"The price is 15 lol")

#Deli
sandwich_orders= ['cheese','pastrami','tomato','pastrami','pastrami', 'bacon','chicken']
finish_orders=[]
print("We are out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print(f"We are now making: {current_orders.title()}")
    finish_orders.append(current_orders)

print("\nThe following orders have been made:")
for order in finish_orders:
    print(order.title(), "Sandwich")
#Dream vaction

responses = {}
active_status = True
while active_status:

    prompt = input("Tell me your name ")
    prompt2 = input("What places do you wanna visit? ")
    responses[prompt] = prompt2

    prompt3 = input("Do you wanna add another user? yes/no")
    if prompt3 == "no":
        active_status=False

print("\nNow the result will be add:")
for k,v in responses.items():
        print(f"Well, {k.title()} choose {v.title()} for their destination")

name=input("What is your name? ")
def greeting(name):
    print(f"\nWelcome, {name.title()} for coming here")

greeting(name)

"""
"""
def make_shirt(size="large", mess="I love python"):
    print(f"So your size is {size.title()} and the message is {mess}")

make_shirt(size="small")

#City Name

def city_country(City, Country):
    fullname = f"Welcome to {City}, {Country}"
    return fullname

print(city_country('Ha Noi', 'Viet Nam'))
"""
#Album
"""
def make_album(Name, Title, Number=None):
    full = {'name': Name, 'title': Title}
    if Number != None:
        full['number'] =Number
    return full

while True:
    n= input(f"Tell me the name")
    if n == 'q':
        break
    t= input(f"Tell me the title")
    if t== 'q':
        break

    the_name = make_album(n,t)
    print(the_name)
"""
"""
#Message

old_mess = ['Hello how are you', 'Fuck You','Bullshit']
new_ones =[]

def  pre_show_mess(old_mess, new_ones):
    while old_mess:
        current_ones= old_mess.pop()
        print(f"\nThe following messages is being processed:{current_ones}")
        new_ones.append(current_ones)

def show_messages(new_ones):
    print("\nHere is the one that's done the proccess:")
    for k in new_ones:
        print(k)
   
pre_show_mess(old_mess,new_ones)
show_messages(new_ones)
#Sandwiches
def items(*sandwich):
    print("Here are the items in your sandwichs: \n")
    for k in sandwich:
        print(f"-{k.title()}")

items('tomamto')
items('bacon', 'cheese')
items('garlic')
#User Profile
def build_profile(first_name, last_name, **user_profile):
    user_profile['firstname']=first_name
    user_profile['lastname']=last_name
    return user_profile

me=build_profile('Nguyen', 'Hieu', location='HaNoi')
print(me)
#Cars
def make_cars(manu, model, *more_info):
    full=manu,model,more_info
    return full

print(make_cars('subaru', 'outback', 'blue'))
"""
"""
import random
random_number = random.randint(1,100)
while random_number:
    prompt = ("You will have to guess a number! ")
    user_input = int(input(prompt))
    if user_input < random_number:
        print("Oh, the number is higher than that!")
    elif user_input > random_number:
        print("Oh my, try lower I guess!")
    else:
        print(f"Bing Bong, the number is {random_number}")
        break
"""
x=12
y=1
print(x,y)
x,y=y,x
print(x,y)

#Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_type=0
    def describe_restaurant(self):
        print(f"Our restaurant's name is {self.name.title()}, and we serve {self.type.title()}")
    def open_restaurant(self):
        print("Our store is now opened!")
    def number_type(self):
        print(f"You have served {self.number_type} people!")
    def set_number_served(self, new_number):
        self.number_type=new_number
    def increse_number(self, increse):
        self.number_type += increse
        

restaurant = Restaurant('New Eridu', 'Japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)
restaurant.increse_number(10000)
print(restaurant.number_type)

#Ice Cream Stand

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Vanila', 'Chocolate']
    def flavour(self):
        for f in self.flavours:
            print(f)

Ic=IceCreamStand("Trang Tien", "IceCream")
Ic.flavour()

#Dice
from random import randint
    
class Dice:
    def __init__(self, sides=6):
        self.sides=sides
    def roll_dice(self):
        print(randint(1, self.sides))

new_dices= Dice(10)
new_dices.roll_dice()
#Users
class Users:
    def __init__(self, first_name, last_name, password, app_number):
        self.first=first_name
        self.last=last_name
        self.passw=password
        self.num=app_number
    def describe_user(self):
        print("Here are the information for the user: \n")
        print("-", self.first)
        print("-", self.last)
        print("-", self.passw)
        print("-", self.num)
    def greet_user(self):
        self.fullname = self.first + " " + self.last
        print(f"Hello, welcome onboard, captain {self.fullname}")


# 9-8. Privileges
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print("Privileges:")
        for p in self.privileges:
            print("-", p)


class Admin(Users):
    def __init__(self, first_name, last_name, password, app_number):
        super().__init__(first_name, last_name, password, app_number)
        self.privileges = Privileges(['add a post', 'delete a post', 'ban a user'])

Admin1 = Admin("Vu", "Minh Long", "281182", "10")
Admin1.privileges.show_privileges()
Admin1.greet_user()
Admin1.describe_user()

# --- Car and ElectricCar Example ---
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
# Battery class with get_range method
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 'an unknown number of'
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size=100
        else:
            print("No need to update!")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())


new_tesla =ElectricCar('tesla', 'model x', '2018')
new_tesla.battery.get_range()
new_tesla.battery.upgrade_battery()
new_tesla.battery.get_range()
"""
with open('pi_million_digits.txt') as file_object:
    contents= file_object.readlines()
pi_strings= ''
for line in contents:
    pi_strings += line.strip()

birthday=input("Enter your birthday: ")

if birthday in contents:
    print("Congrats, your birthday is in first million of pi digits!")
else:
    print("too bad lol"


text_file = 'programming.txt'
with open(text_file, 'a') as file_object:
    file_object.write("I love big boobs\n")

#Add new users in txt
filename ='guests.txt'
with open(filename, 'a') as file_object:
    prompt= "Tell me your name: "
    prompt += "type q to quit:"
    while True:
        users = []
        users=input(prompt)
        if users == 'q':
            break
        else:
            file_object.write(f"{users}\n")


filename= 'alice.txt'
with open(filename, encoding='utf-8') as file_objects:
    contents= file_objects.read()
    line = contents.split()
    num= len(line)
    print(f"The file has {num} words")
#Addition
while True:
    First= input("Enter your first numb: ")
    if First == 'q':
        break
    Sec= input("Enter your second num: ")
    if Sec == 'q':
        break
    try: 
        addition = int(First) + int(Sec)
        print(addition)
    except ValueError:
        print("Hell nah, try to enter a number lol")

#Storing and Greeting new users
import json
def greet_user():
    filename= 'username.txt'
    try:
        with open(filename) as f:
            username=json.load(f)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        username=input("What is your name: ")
        with open(filename, 'w') as f: 
            json.dump(username, f)
            print(f"Welcome {username}, we will remember you next time")
    else:
        print(f"Welcome back, {username}")

import json 

filename = 'user_fav.txt'

try:
    with open(filename) as f:
        favs= json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    with open(filename, 'w') as f:
        fav=input('Tell me your favourite number: ')
        json.dump(int(fav), f)
        print(f"So your favourite number is {fav}! ")
else: 
    with open(filename) as f:
        favs= json.load(f)
        print(f"You already have a favourite number! It's {favs}")
    
#City, country for testing
def cityandcountry(City, Country, population= ''):
    fullname=f"{City.title()}, {Country.title()} - population {population}"
    return fullname
import unittest
class NameTest(unittest.TestCase):

    def test_cityandcountry(self):
        formatted= cityandcountry('hanoi', 'vietnam')
        self.assertEqual(formatted, 'Hanoi, Vietnam - population ')
    def test_cityandcountrypop(self):
        formatted=cityandcountry('laocai', 'vietnam', '100000')
        self.assertEqual(formatted, 'Laocai, Vietnam - population 100000')

if __name__ == '__main__':
    unittest.main()
"""
#Testing Employee
class Employee():
    def __init__(self, first, last, annual):
        self.firstname = first
        self.lastname = last
        self.money=int(annual)
    def give_raise(self, money=5000):
        self.money += money
    def __str__(self):
        return (f"{self.firstname} {self.lastname}:{self.money}")
        
import unittest
from random import randint

class TestEmployee(unittest.TestCase):
    #Define instance
    def setUp(self):
        self.emp = Employee('Nguyen', 'Trung Hieu', '5000')
    def test_default_value(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.money, 10000)
    def test_random_value(self):
        self.addnumber =randint(1000, 2000)
        self.emp.give_raise(self.addnumber)
        self.assertEqual(self.emp.money, 5000 + self.addnumber)

if __name__ == '__main__':
    unittest.main()


        
        

        







 


