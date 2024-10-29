# https://www.acmicpc.net/problem/1932

N = int(input())
dp = [[0] * i for i in range(1, N+1)]
triangle = []
for i in range(N): 
  if i == 0:
    triangle.append([int(input())])
  else:
    triangle.append(list(map(int, input().split(" "))))

for i in range(N):
  for j in range(i+1):
    if i==j:
      dp[i][j] = dp[i-1][j-1]+triangle[i][j]
    elif j==0:
      dp[i][j] = dp[i-1][0] + triangle[i][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]
print(max(dp[N-1]))