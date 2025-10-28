import math
t = int(input())
for _ in range(t):
    co_so_dich = int(input())
    nhiphan = list((input()))
    dodai = len(nhiphan)
    k = int(math.log2(co_so_dich))
    so_du = int(dodai % k)
    res = 0
    list_res = []
#Fix boso
    if so_du != 0:
        boso = int(dodai / k) +1
    else:
        boso = int(dodai / k)
#them so 0
    if so_du !=0:
        nhiphan = ['0'] * (k-so_du) + nhiphan
#Pop so nhi phan
    for i in range(boso):
        current_list = nhiphan[-k:]
        nhiphan = nhiphan[:-k]
#chuyenheso
        for i in range(0,k):
            bit = int(current_list[i])
            res += bit * (2**(k-i-1))
        list_res.insert(0,res)
        res= 0
    print(*list_res, sep="")








