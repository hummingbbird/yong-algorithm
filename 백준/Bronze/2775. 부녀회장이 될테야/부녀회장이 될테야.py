# https://www.acmicpc.net/problem/2775

T = int(input())

for _ in range(T):
  k = int(input())
  n = int(input())
  dp = [[0]*n for _ in range(k+1)]
  # print(dp)
  for i in range(k+1): # 0~k
    for j in range(n):
      if i==0:
        dp[i][j] = j+1
      elif j==0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
  print(dp[i][j])
        