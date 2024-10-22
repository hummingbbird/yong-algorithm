import sys

N = int(sys.stdin.readline())
# nums = [int(sys.stdin.readline()) for _ in range(N)]
nums = list(map(int, sys.stdin.readline().split(" ")))

dp = nums[:] # 이렇게 하면 깊은 복사
# dp=num # 이렇게 하면 얕은 복사!! 주의하기!!

for i in range(1, N):
  for j in range(i+1):
    if nums[i]>nums[j]:
      dp[i] = max(dp[j]+nums[i], dp[i])
  
print(max(dp))