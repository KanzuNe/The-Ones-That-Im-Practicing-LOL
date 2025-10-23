"""
org_lst = []
num = int(input())
intp= (input())
fin_lst = intp.split()
s = map(int,fin_lst)


for index in s:
    org_lst.append(index)
n = 0
while n < len(org_lst) -1:
        g= (org_lst[n] + org_lst[n+1])
        if g %2 ==0:
                org_lst.remove(org_lst[n+1])
                org_lst.remove(org_lst[n])
        else:
            n +=1       
        

print(len(org_lst))
"""
n = int(input())
other_lst = []
A = input()
lst = A.split()
print(lst)
s = map(int, lst)
for x in s:
    other_lst.append(x)
print(other_lst)
i = 0
while i < len(other_lst)-1:
    if (other_lst[i] + other_lst[i+1]) % 2 == 0:
        print(other_lst[i], other_lst[i+1])
        other_lst.remove(other_lst[i+1])
        other_lst.remove(other_lst[i])
        
    else:
        i += 1
print(len(other_lst))





    

