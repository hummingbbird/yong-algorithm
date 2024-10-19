def solution(m, n, puddles):
    answer = 0
    dp = [[1]*m for _ in range(n)]
    for i in range(len(puddles)):
        x, y = puddles[i][1]-1, puddles[i][0]-1
        dp[x][y]=0
    print(dp)
    for i in range(n):
        for j in range(m):
            # 가장 첫번째 칸은 continue
            if i==0 and j==0:
                continue
            # 웅덩이는 0
            if dp[i][j] == 0:
                continue
            #테두리인데 앞에 0이 있었어 -> 뒤는 다 0이야
            if (i==0 and dp[i][j-1]==0) or (j==0 and dp[i-1][j]==0): 
                dp[i][j] = 0
            # 그 외 테두리가 아닌 경우에만 덧셈 연산
            elif i!=0 and j!=0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            # print(f"dp[{i}][{j}] = {dp[i][j]}")
    
    return dp[n-1][m-1]%1000000007