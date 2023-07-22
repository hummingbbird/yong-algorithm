while True:
    tran = list(map(int, input().split()))
    if sum(tran)==0:
        break
    tran=sorted(tran)
    if tran[0]+tran[1]<=tran[2]:
        print("Invalid")
    elif tran[0]==tran[1] and tran[1]==tran[2]:
        print("Equilateral")
    elif tran[0]==tran[1] or tran[1]==tran[2] or tran[2]==tran[0]:
        print("Isosceles")
    else:
        print("Scalene")