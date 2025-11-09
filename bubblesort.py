"""
n = int(input().strip())
initial = list(map(int,input().split()))
Process = True
counter = 0
while Process:
    swapped = False
    i = 1
    while i <n:
        if initial[i-1] > initial[i]:
            initial[i-1], initial[i] = initial[i], initial[i-1]
            swapped = True
        i+=1
    if swapped:
            counter +=1
            print(f"Buoc {counter}:", *initial, sep=" ")
    else:
        Process = False         
"""
N = int(input())
a = list(map(int, input().split()))[:N]
t = 0
if a == sorted(a):
    s = map(str, a)
    A = ' '.join(s)
    t += 1
    T = f'{t}:'
    print('Buoc', T, A)
else:
    while True:
        changed = False
        for i in range(len(a) - 1):



            if a[i] > a[i + 1]:
                for j in range(i + 1, len(a)):

                    if a[i] <= a[j]:
                        a.insert(j, a[i])
                        a.remove(a[i])
                        changed = True
                        break


                    if a[i] > a[j]:
                        if j == len(a) - 1:
                            a.append(a[i])
                            a.remove(a[i])
                            changed = True
                            break

                        elif j < len(a) + 1:
                            continue


            if changed:
                if i == len(a) - 2:
                    s = map(str, a)
                    A = ' '.join(s)
                    t += 1
                    T = f'{t}:'
                    print('Buoc', T, A)
                elif i < len(a) - 2:
                    continue


            elif a[i] <= a[i + 1]:
                continue

        if not changed:
            break
