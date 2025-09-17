n, k = map(int, input().split())
wv = [[0,0]]

for _ in range(n):
    wv.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = wv[i][0], wv[i][1]
    for j in range(1, k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-w]+v)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][k])