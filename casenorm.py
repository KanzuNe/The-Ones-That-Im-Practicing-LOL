n = input()
upper = sum(1 for char in n if char.isupper())
lower = sum(1 for char in n if char.islower())
if lower >= upper:
    print(n.lower())
else:
    print(n.upper())