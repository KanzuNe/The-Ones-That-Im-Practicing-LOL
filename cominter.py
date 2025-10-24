import math
T = int(input())
for _ in range(T):
    N, X, M = map(float, input().split())
    if N>=M:
        print(0)
    else:
        so_nam = math.log(M/N,1+X/100)
        result = so_nam
        if N * ((1 + X/100) ** result) < M:
            result += 1
        
        print(int(result))

