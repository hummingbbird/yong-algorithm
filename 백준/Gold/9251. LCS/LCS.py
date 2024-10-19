import sys
sys.setrecursionlimit(10**7)

A = input()
B = input()
m, n = len(B), len(A)
dp = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if i==0 and j==0 and A[i]==B[j]:
      dp[0][0]=1
    if A[i] == B[j]:
      # 테두리일 경우 1로 설정(아닌 건 0이니까)
      if i == 0 or j==0:
        dp[i][j] = 1
      # 둘이 같은데 테두리 아니야
      else:
        dp[i][j]=dp[i-1][j-1]+1
    # 둘이 달라
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[n-1][m-1])