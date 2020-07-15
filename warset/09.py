def to_int(x): return int(x)


def vertical(n, m, dots):
    a, b = n - 1, m - 1
    for i in range(n):
        for j in range(m // 2):
            if dots[i][j] != dots[i][b - j]:
                return False
    return True


def horizontal(n, m, dots):
    a, b = n - 1, m - 1
    for i in range(n // 2):
        for j in range(m):
            if dots[i][j] != dots[a - i][j]:
                return False
    return True


def point(n, m, dots):
    a, b = n - 1, m - 1
    for i in range(a):
        for j in range(b):
            if dots[i][j] != dots[a - i][b - j]:
                return False
    return True


n, m = map(to_int, input().split(" "))
dots: list = []
for _ in range(n):
    dots.append(input())

res: list = []
if vertical(n, m, dots) or horizontal(n, m, dots):
    res.append("line")
if point(n, m, dots):
    res.append("point")

if len(res) > 0:
    print("%s symmetry" % ' '.join(res))
else:
    print("none")
