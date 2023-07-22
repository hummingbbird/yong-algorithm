tran = list(map(int, input().split()))
tran = sorted(tran)
if tran[0]+tran[1]>tran[2]:
    print(sum(tran))
else:
    print(tran[0]+tran[1]+tran[0]+tran[1]-1)