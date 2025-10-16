import math
a,b,c = map(float, input().split())

if a==0 and b==0 and c==0:
    print("VSN")
elif a==0:
    res=-c/b
    print(round(res, 6))
elif a!=0:
    delta= b**2- 4*a*c
    if delta <0:
        print("VN")
    elif delta==0:
        res=-b/(2*a)
        print(round(res,6))
    elif delta >0:
        delta_sqrt = math.sqrt(delta)
        res1= (-b + delta_sqrt)/(2*a)
        res2= (-b - delta_sqrt)/(2*a)
        h=[round(res1,6), round(res2,6)]
        h.sort()
        print(h[0], h[1])


        

