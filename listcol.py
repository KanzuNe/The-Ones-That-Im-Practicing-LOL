
n = int(input())
other_lst = []
A = input()
lst = A.split()
s = map(int, lst)
for x in s:
    other_lst.append(x)
res = []
for a in other_lst:
    if res:
        phan_tu_cuoi = res[-1]
        if (phan_tu_cuoi + a) %2 == 0:
            res.pop(-1)
        else:
            res.append(a)
    else:
        res.append(a)
print(len(res))





    

