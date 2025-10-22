import math
T=int(input())
for _ in range(T):
    a= int(input())
    k= int(math.log2(a-1))
    

    ssh_csc= a
    tong_csn = (1-(2**(k+1)))/(1-2)

    tong_csc = (ssh_csc*(1+a))/2
    res= tong_csc -(2*tong_csn)
    print(int(res))