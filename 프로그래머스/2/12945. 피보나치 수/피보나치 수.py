def solution(n):
    ans = [0 for i in range(n+1)]
    for i in range(n+1):
        if  i == 0 or i == 1:
            ans[i] = i
        else:
            ans[i] = ans[i-1] + ans[i-2]
    return ans[-1] % 1234567
    
    