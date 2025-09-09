


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

squares=[]
for value in range(1, 21):
    square = value ** 2
    
    squares.append(square)
print(squares)

million =[value for value in range(1, 1_000_001)]
print(sum(million))

x3 =[value*3 for value in range(1, 31)]
print(x3)

cubes= [value**3 for value in range(1, 11)]
print(cubes) 