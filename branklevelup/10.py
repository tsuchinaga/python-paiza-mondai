dots: list = []
for _ in range(5):
    for c in input():
        dots.append(c)

for hit in [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [0, 5, 10, 15, 20],
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 14, 19, 24],
    [0, 6, 12, 18, 24],
    [4, 8, 12, 16, 20],
]:
    t = 0
    for h in hit:
        if dots[h] == "X":
            t -= 1
        if dots[h] == "O":
            t += 1
    if t == 5:
        print("O")
        exit(0)
    if t == -5:
        print("X")
        exit(0)
print("D")
