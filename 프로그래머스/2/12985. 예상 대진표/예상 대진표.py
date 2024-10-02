def change(num):
    if num==1:
        return 1
    elif num%2 == 0:
        return num//2
    else:
        return (num//2)+1
    
def solution(n,a,b):
    answer = 1
    # 종료조건을 찾아라!
    while (a>2 or b>2):
    # while ((a-b)!=1 and (b-a)!=1):
        print(a, b)
        a, b = change(a), change(b)
        if a==b:
            return answer
        answer+=1
    return answer