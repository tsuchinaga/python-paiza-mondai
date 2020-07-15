cs = {}
for _ in range(int(input())):
    c = input()
    if c in cs:
        print("NO")
    else:
        cs[c] = True
        print("YES")
