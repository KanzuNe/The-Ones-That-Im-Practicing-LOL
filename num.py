"""
num = int(input("Input a number between 1 and 10^9: "))

if num >1 and num <=10**9:
    if num % 2 == 0:
        total = sum(range(1, num, 2)) 
        print(total)
    else:
        total = sum(range(1, num + 1, 2))
        print(total)
   
else:
    print("This number exceed the limit of the calculator, please enter another one")

new_num = int(input())
length = (new_num - 1)/2 +1
res = (1 + new_num) * length /2

print(res)
"""

def dut_result(x,y,z,k):
    float(x),float(y),float(z)
    int(k)
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
    return dut

result = dut_result(7,5,5.5,2)
print(round(result,2))




