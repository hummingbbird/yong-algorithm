def solution(n):
    ans=0
    #1.3진법으로 표현하기
    lst=[]
    while n>=3:
        lst.append(str(n%3))
        n=n//3
    lst.append(str(n))
    
    #2.앞뒤반전해서 문자열로
    strN = ''.join(lst)[::-1]
    
    #.3.10진법으로 다시 나타내기
    for i in range(len(strN)):
        ans += int(strN[i])*(3**i)
    
    
    return ans

