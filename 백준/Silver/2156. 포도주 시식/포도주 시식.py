import sys
n = int(sys.stdin.readline())
wines = [int(sys.stdin.readline()) for _ in range(n)]
dp = wines[:]

for i in range(n):
  if i<2:
    dp[i] = sum(dp[:i+1])
  elif i == 2: 
    dp[i] = max(wines[i-2]+wines[i], wines[i-1]+wines[i], dp[i-1])
  else:
    candidate = max(dp[i-3]+wines[i-1]+ wines[i], dp[i-2]+ wines[i])
    dp[i] = max(max(dp[:i]), candidate)
print(max(dp))