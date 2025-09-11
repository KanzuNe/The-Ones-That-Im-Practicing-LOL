


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
        print()
