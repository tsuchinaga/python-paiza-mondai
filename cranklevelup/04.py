def to_int(x):
    return int(x)


n = int(input())
l = []
for _ in range(n):
    g, s = map(to_int, input().split(" "))
    l.append("%02d:%02d" % (s, g))
for ans in sorted(l, reverse=True):
    s, g = map(to_int, ans.split(":"))
    print("%d %d" % (g, s))
