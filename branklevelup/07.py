n = int(input())
l: list = []
for _ in range(n):
    s, d = input().split(" ")
    l.append([s, int(d)])

while len(l) > 0:
    maxI = 0
    for i in range(len(l)):
        if l[maxI][1] > l[i][1]:
            maxI = i
    print(l[maxI][0])
    l.pop(maxI)
