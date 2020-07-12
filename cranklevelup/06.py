h = int(input())
ad: list = []
bd: list = []

i = 0
while h > 0:
    a = 1
    b = 1
    if i >= 2:
        a = bd[i - 1] + bd[i - 2]
        b = ad[i - 1] * 2 + ad[i - 2]

    h -= b
    ad.append(a)
    bd.append(b)
    i += 1

print(i)
