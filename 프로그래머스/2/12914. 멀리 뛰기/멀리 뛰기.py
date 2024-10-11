def solution(n):
    # 재귀문제랑 머가다르니
    # 기본 구조: solution(n) = solution(n-1) + solution(n-2)
    dp=[0 for i in range(n+1)]
    
    for i in range(1,n+1):
        if i == 1 or i==2:
            dp[i] = i
        else:
            dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]%1234567
        