x = float(input("s1: "))
y = float(input("s2 : "))
z = float(input('s3:'))
k = int(input('khu vuc:'))


tong_diem = x + y + z
dut = 0
if tong_diem >=22.5:
    if k ==1:
            dut = ((30-tong_diem)/7.5)*0.75
    elif k ==2:
            dut = ((30-tong_diem)/7.5)*0.5
    elif k ==3:
            dut = ((30-tong_diem)/7.5)*0
else:
    if k ==1:
            dut +=0.75
    elif k ==2:
            dut +=0.5
    elif k ==3:
            dut +=0

print(round(dut,2))