def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def cong_pt(a,b,c,d):
    res_a, res_b = (a*d)+(b*c), (b*d)
    return res_a, res_b




a,b,c,d = map(int, input().split())
res_a, res_b = cong_pt(a,b,c,d)
ucn = gcd(res_a,res_b)

print(f"{int(res_a/ucn)}/{int(res_b/ucn)}")