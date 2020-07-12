def to_int(x):
    return int(x)


n = int(input())
for _ in range(n):
    t, h, m = input().split(" ")
    th, tm = map(to_int, t.split(":"))
    tm += int(m)
    th = (th + int(h) + tm // 60) % 24
    tm = tm % 60
    print("%02d:%02d" % (th, tm))
