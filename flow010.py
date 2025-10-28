def solve():
    # Viết giải pháp
    t = int(input())
    for _ in range(t):
        n = input().lower()
        if n == "b":
            print("BattleShip")
        elif n == "c":
            print("Cruiser")
        elif n == "d":
            print("Destroyer")
        elif n == "f":
            print("Frigate")
    pass

if __name__ == "__main__":
    solve()
