n = int(input())
dic = {}
for _ in range(n):
    s, d = input().split(" ")
    if s not in dic:
        dic[s] = 0
    dic[s] += int(d)

while len(dic) > 0:
    maxK = ""
    for k in dic:
        if maxK == "" or dic[maxK] < dic[k]:
            maxK = k
    print("%s %d" % (maxK, dic[maxK]))
    dic.pop(maxK)
