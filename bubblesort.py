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

