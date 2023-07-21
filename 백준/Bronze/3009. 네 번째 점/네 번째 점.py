xLst={}
yLst={}
for _ in range(3):
    x, y = map(int, input().split())
    if not x in xLst:
        xLst[x] = 1
    else:
        xLst[x]+=1
    if not y in yLst:
        yLst[y] = 1
    else:
        yLst[y]+=1
print(list(k for k, v in xLst.items() if v == 1)[0],end=' ')
print(list(k for k, v in yLst.items() if v == 1)[0])