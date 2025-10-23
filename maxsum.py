### write your code here...

T= int(input())
for _ in range(T):
    str= input()
    current_num= ""
    number=[]
    for char in str:
        if char.isdigit():
            current_num += char
            print(current_num)
        else:
            if current_num:
                number.append(int(current_num))
                print(number)
                current_num=""
    

    print(max(number)) 
    


    
