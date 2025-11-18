N = int(input())
for _ in range (N):
    buoc = 0
    chuoi = list(input().split())
    a = len(chuoi)
    for i in range(a - 1):
        swapped = False
        for j in range(a - i - 1):
            if chuoi[j] > chuoi[j + 1]:
                chuoi[j], chuoi[j + 1] = chuoi[j + 1], chuoi[j]
                swapped = True
            if swapped:
                buoc += 1
                print("Buoc", buoc, ":", chuoi)
