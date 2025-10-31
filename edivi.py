# write your code here...
t = int(input())
res =  []
for _ in range(t):
    n = int(input())
    for i in range(1,n+1):
        if n % i ==0:
            current_num = i
            if current_num % 2 == 0:
                res.append(current_num)
    print(len(res))
    res.clear()