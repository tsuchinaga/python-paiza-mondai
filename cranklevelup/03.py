def to_int(x):
    return int(x)


n, m, k = map(to_int, input().split(" "))
for _ in range(n):
    ans = 0
    for a in map(to_int, input().split(" ")):
        if k == a:
            ans += 1
    print(ans)
