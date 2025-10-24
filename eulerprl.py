t = int(input())
for _ in range(t):
    n = int(input())
    ssh = n-1
    num = 2
    snt = True
    if ssh == 0 or ssh ==1:
        print("NO")
    while num < ssh-1:
        if ssh % num == 0:
            snt = False
            break
        num +=1

    if snt:
        print("YES")
    else:
        print("NO")


        


        

