def to_int(x):
    return int(x)


p, q, r = map(to_int, input().split(" "))
pq = {}
qr = {}
for _ in range(p):
    i, j = map(to_int, input().split(" "))
    pq[i] = j

for _ in range(q):
    i, j = map(to_int, input().split(" "))
    qr[i] = j

for n in range(p):
    print("%d %d" % (n + 1, qr[pq[n + 1]]))
