n = int(input())
nums = [int(input()) for _ in range(n)]
# nums = [10, 20, 15,25,10,20]
dp = [0 for _ in range(n)]

if n==1 or n==2:
  print(sum(nums))
else:
  dp[0] = nums[0]
  dp[1] = nums[0]+nums[1]
  for i in range(2, n):
    dp[i] = max(dp[i-3]+nums[i-1]+nums[i], dp[i-2]+nums[i])
  
  print(dp[-1])

