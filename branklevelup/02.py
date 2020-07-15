def to_int(x): return int(x)


n = int(input())
ans = 0
for _ in range(n):
    a, b = map(to_int, input().split(" "))
    if a == b:
        ans += a * b
    else:
        ans += a + b
print(ans)
