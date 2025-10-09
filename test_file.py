# Nhập code của bạn ở đây\
"""
import math

def distance(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    # Viết giải pháp
T = int(input())

for _ in range(T):
    R = float(input())
    x1,y1 = map(float, input().split())
    x2,y2 = map(float, input().split())
    x3,y3 = map(float, input().split())
    d12 = distance(x1,y1,x2, y2)
    d13 = distance(x1,y1, x3, y3)
    d23 = distance(x2,y2, x3, y3)

    res = False
    if d12 <=R and d23<=R and d13<=R:
        res= True
    if d12 >= R:
        if d13 <= R and d23 <= R:
            res= True
    
    if d13 >=R:
        if d12<=R and d23<=R:
            res = True
    if d23 >=R:
        if d13 <=R and d12 <= R:
            res=True

    
    if res== True:
            print("yes")
    else:
            print("no")
"""





    
