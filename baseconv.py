"""
import math
t = int(input())
for _ in range(t):
    co_so_dich = int(input())
    nhiphan = list((input()).strip())
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
            if res<10:
                list_res.insert(0,res)
                res= 0
            else:
                list_res.insert(0, chr(ord('A')+res-10))
                res=0
    print(*list_res, sep="")
"""

import math

T = int(input())
for _ in range(T):
    b = int(input())
    k = int(math.log2(b))
    bin_str = input().strip()
    length = len(bin_str)
    
    # Thêm số 0 vào ĐẦU (không cần đảo!)
    so_du = length % k
    if so_du != 0:
        bin_str = '0' * (k - so_du) + bin_str
    
    # Cắt thành chunks (từ trái sang phải)
    chunks = []
    for i in range(0, len(bin_str), k):
        chunks.append(bin_str[i:i+k])
    
    # Chuyển sang hệ b
    res = []
    for chunk in chunks:
        ints = int(chunk, 2)
        if ints < 10:
            res.append(str(ints))
        else:
            res.append(chr(ints - 10 + ord('A')))
    
    print(''.join(res))







