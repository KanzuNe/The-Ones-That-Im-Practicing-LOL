# write your code here...
import sys
for line in sys.stdin:
    number = line.strip()
    four = number.count("4")
    seven = number.count("7")
    total = four + seven
    if total == 4 or total == 7:
        print("YES")
    else:
        print("NO")
        