


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

user_names=['admin', 'user1', 'user2', 'user3', 'user4']
for user_name in user_names:
    if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
    elif user_name != 'admin':
            print(f"Hello {user_name}, thank you for log in again!")
    else:
            print("We need to find some users!")
print("\nThat's it!")
