import math
a,b,c = map(float, input().split())

if a==0 and b==0 and c==0:
    print("VSN")
elif a==0 and b==0 and c!=0:
    print("VN")
elif a==0 and b!=0 and c==0:
    print(0)
elif a==0 and b!=0 and c!=0:
    res=-c/b
    print(f"{res:.6f}")
elif a!=0:
    delta= b**2- 4*a*c
    if delta <0:
        print("VN")
    elif delta==0:
        res=-b/(2*a)
        print(f"{res:.6f}")
    elif delta >0:
        delta_sqrt = math.sqrt(delta)
        res1= (-b + delta_sqrt)/(2*a)
        res2= (-b - delta_sqrt)/(2*a)
        h=[res1, res2] 
        print(f"{h[0]:.6f} {h[1]:.6f}") 

