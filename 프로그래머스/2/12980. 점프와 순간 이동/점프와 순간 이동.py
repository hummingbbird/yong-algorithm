def jaegui(n):
    if n==1 or n==2:
        return 1
    elif n%2 == 0:
        return jaegui(n//2)
    else:
        return jaegui(n-1)+1

def solution(n):
    if n==1 or n==2:
        return 1
    elif n%2 == 0:
        return solution(n//2)
    else:
        return solution(n-1)+1
    return solution(n)
    