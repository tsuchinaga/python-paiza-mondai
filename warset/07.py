l: list = []

for _ in range(int(input())):
    a = int(input())
    if a % 2 == 1:
        l.append(a)

for a in sorted(l):
    print(a)
