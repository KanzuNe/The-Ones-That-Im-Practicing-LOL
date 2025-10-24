t = int(input())
for _ in range(t):
    num_of_acts,nation = map(str, input().split())
    num_of_acts = int(num_of_acts)
    total_prize = 0
    for _ in range(num_of_acts):
        act_input = input().split()
        first = act_input[0]
        if first == "CONTEST_WON" or first == "BUG_FOUND":
            sec = int(act_input[1])
        else:
            sec = None
        if first == "CONTEST_WON":
            if sec <= 20:
                total_prize += 300 + 20-sec
            else:
                total_prize +=300
        elif first == "TOP_CONTRIBUTOR":
            total_prize += 300
        elif first == "BUG_FOUND":
            total_prize += sec
        elif first == "CONTEST_HOSTED":
            total_prize += 50


    if nation == "INDIAN":
        remainder = total_prize % 200
        result = int(total_prize / 200)
        final = (total_prize - remainder)/200
        print(int(final))

    elif nation == "NON_INDIAN":
        remainder = total_prize %400
        result= int(total_prize) /400
        final = (total_prize - remainder)/400
        print(int(final))
        





            



        
