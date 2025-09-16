

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
