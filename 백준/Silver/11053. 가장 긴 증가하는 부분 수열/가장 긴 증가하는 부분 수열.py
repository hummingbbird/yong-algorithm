N = int(input())
A = list(map(int, input().split(" ")))
answer=0
dp = [1] * N

for i in range(1, N):
  for j in range(i):
    if A[j]<A[i]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))