def solution(a):
    if a==1:
        return 1
    elif a>1 and a<8:
        return 2
    else:
        n = 0
        Sn = 3*n*(n+1)+1
        while Sn < a:
            Sn = 3*n*(n+1)+1
            n += 1
        return n


a = int(input())
print(solution(a))
