# write your code here...
t= int(input())
for _ in range(t):
    n,d = map(int, input().split())
    str = list(input().split())
    moved = []
    for i in range(d):
        moved.append(str[i])

    res = str[d:] + moved
    print(' '.join(res))