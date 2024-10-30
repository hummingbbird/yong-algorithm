# https://www.acmicpc.net/problem/1149
N = int(input())
dp=[[0]*3 for _ in range(N)]
RGB = []
result=[] # 집의 최솟값을 누적
for _ in range(N):
  rgb = list(map(int, input().split(" ")))
  RGB.append(rgb)
  
min_idx = RGB[0].index(min(RGB[0]))

for i in range(N):
  if i>0:
    min_idx = dp[i-1].index(min(dp[i-1]))
  for j in range(3):
    if i == 0:
      dp[i][j] = RGB[i][j]
    elif min_idx != j:
      dp[i][j] = RGB[i][j] + dp[i-1][min_idx]
    else: # 전 min랑 지금 idx랑 같은 경우
      if min_idx == 0:
        dp[i][j] = RGB[i][j] + min(dp[i-1][1], dp[i-1][2])
      elif min_idx == 1: 
        dp[i][j] = RGB[i][j] + min(dp[i-1][0], dp[i-1][2])
      else: 
        dp[i][j] = RGB[i][j] + min(dp[i-1][0], dp[i-1][1])
  result.append(min(dp[i]))

print(min(dp[i]))