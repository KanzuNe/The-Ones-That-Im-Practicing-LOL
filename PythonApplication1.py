


from encodings.punycode import T
import pprint
from xml.etree.ElementInclude import LimitedRecursiveIncludeError


guest_list = ['Alice', 'Bob', 'Charlie', 'David']
guest_list.sort(reverse=True)
print(guest_list)

gpu = ["4080 super", "5090", "1660 super", "5080"]
gpu.reverse()
print(gpu)

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

alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
        print("You just earned 5 points")
else :
        print("\n")

user_names=[]
for user_name in user_names:
    if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
    else:
            print("We need to find some users!")
print("\nThat's it!")

current_users = [' Alice', 'David', 'Homie','Belle']
new_users=['Admin', 'Miyabi', 'Belle']
#For casesensitive
current_lower_users = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_lower_users:
        print(f"Sorry, {new_user} have already been taken")
    else:
        print(f"Good, the name {new_user} is available")

ordinal_numbers= [range(1,10)]
for ordinal_number in ordinal_numbers:
    if ordinal_numbers == 1:
                print("1st")
    elif ordinal_number == 2:
                print("2nd")
    elif ordinal_number == 3:
                print("3rd")
    else: 
        print(f"{ordinal_number}th")
