"""
num = int(input("Input a number between 1 and 10^9: "))

if num >1 and num <=10**9:
    if num % 2 == 0:
        total = sum(range(1, num, 2)) 
        print(total)
    else:
        total = sum(range(1, num + 1, 2))
        print(total)
   
else:
    print("This number exceed the limit of the calculator, please enter another one")
"""
new_num = int(input())
length = (new_num - 1)/2 +1
res = (1 + new_num) * length /2

print(res)




