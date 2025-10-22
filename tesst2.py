### write your code here...

T= int(input())
for _ in range(T):
    str= input()
    current_num= ""
    number=[]
    for char in str:
        if char.isdigit() == True:
            number += char
        else:
            number.append(" ")
        s= "".join(number)
        lsr = s.split()
print(s)
print(lsr)
print(max(map(int, lsr)))

"""

    for char in str:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                number.append(int(current_num))
                current_num=""
    

    print(max(number)) 
"""

