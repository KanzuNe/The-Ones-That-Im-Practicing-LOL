
t = int(input())
for _ in range(t):
    N,X,M = map(float, input().split())
    t = 0
    z = True
    while z:
        result = N * (1+X/100)**t
        if round(result,2) >=M:
            print(t)
            z= False
        else:
            t +=1

