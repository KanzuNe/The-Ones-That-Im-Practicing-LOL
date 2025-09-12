


#Oh yes, the guest list
guest_list = ['Alice', 'Bob', 'Charlie', 'David']
guest_list.sort(reverse=True)
print(guest_list)
#Uh, dont bother ask me
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
        print(f"{name}'s favourite places is {places}")


