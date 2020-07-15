s = input()
t = input()
ans = 0
for i in range(len(t) - len(s) + 1):
    if s == t[i:i + len(s)]:
        ans += 1
print(ans)
