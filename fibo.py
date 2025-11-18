import math
t = int(input())
for _ in range(t):
    n= 0
    formula = (1/math.sqrt(5))*(((1+math.sqrt(5)/2)**n)-((1-math.sqrt(5))/2)**n)
    user = int(input())
    
    while formula != user:
        n +=1
        if formula == user:
            print("Yes")
        else:
            print("No")