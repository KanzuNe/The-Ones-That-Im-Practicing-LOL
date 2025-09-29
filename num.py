num = input("Input a number between 1 and 10^9: ")
num_int = int(num)
if num_int >1 and num_int <=10**9:
    if num_int % 2 == 0:
        total = sum(range(1, num_int, 2)) 
        print(total)
    else:
        total = sum(range(1, num_int + 1, 2))
        print(total)
   
else:
    print("Sai số rồi ccho này")




