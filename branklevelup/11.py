names: list = []
nb = {}
br = {}

for _ in range(int(input())):
    u, b = input().split(" ")
    names.append(u)
    nb[u] = b

for _ in range(int(input())):
    b, r = input().split(" ")
    br[b] = r

for name in names:
    print("%s %s" % (name, br[nb[name]]))
