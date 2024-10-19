def solution(triangle):
    answer = 0
    height = len(triangle)
    dp = [[0]*n for n in range(1, height+1)]
    for i in range(height):
        for j in range(i+1):
            if i==0: # 꼭대기: 그대로
                dp[i][j]=triangle[0][0]
            elif i==j: # 오른쪽 끝: 위에 거
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            elif j==0:# 왼쪽 끝: 위에 거
                dp[i][j] = dp[i-1][0]+triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]
    return max(max(dp))