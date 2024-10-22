# https://www.acmicpc.net/problem/11722
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(" ")))
dp = [1]*N

for i in range(N):
  for j in range(i):
    if A[j]>A[i]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
