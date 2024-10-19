n = int(input())
matrix = [tuple(map(int, input().split())) for i in range(n)]

dp = [[0]*n for i in range(n)]
for count in range(n-1):
    for i in range(n-1-count):
        j = i+count+1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])
print(dp[0][-1])