def to_int(x): return int(x)


a, b = map(to_int, input().split(" "))
s = input()
print(s[a-1:b])
