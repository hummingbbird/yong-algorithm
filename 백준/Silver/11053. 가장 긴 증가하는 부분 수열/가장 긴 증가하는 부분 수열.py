a = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(a)]

for i in range(a): #i = 0~a-1까지 반복
 for j in range(0, i):
  # 대상이 되는 숫자(i)가 전 숫자(j)보다 작으면 dp값 비교
  if lst[i] > lst[j]:
   dp[i] = max(dp[i], dp[j]+1)



print(max(dp))
