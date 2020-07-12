n = int(input())
for _ in range(n):
    s = input().split(" ")
    print("%s %d" % (s[0], int(s[1]) + 1))
