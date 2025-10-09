a,b,c = map(int,input().split())

ketqua = []

for tong_chu_so in range (1, 100):
    x = b* (tong_chu_so**a) +c

    if x>=1 and x <= 10**9:
        str_x= str(x)
        tong_thuc_te= 0

        for chu_so in str_x:
            tong_thuc_te += int(chu_so)

        if tong_chu_so == tong_thuc_te:
            ketqua.append(x)

print(len(ketqua))
ketqua.sort()
print(*ketqua)
