number = int(input())
n = list((input().split()))
list_con = []
list_con.append(n[0])
print(f"Buoc 0: {n[0]}")
del n[0]
counter = 0
for _ in range(len(n)):
    for g in range(len(list_con)):
                if n[0] <= list_con[g]:
                    list_con.insert(g, n[0])
                    n.pop(0)
                    counter +=1
                    print(f"Buoc {counter}:", *list_con, sep=" ")
                    break
                elif g == len(list_con)-1 :
                    list_con.insert(g+1, n[0])
                    n.pop(0)
                    counter +=1
                    print(f"Buoc {counter}:", *list_con, sep=" ")
                    break



