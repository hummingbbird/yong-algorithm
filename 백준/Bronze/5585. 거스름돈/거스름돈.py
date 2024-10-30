# https://www.acmicpc.net/problem/5585
money = int(input())
jandon = 1000-money
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

# for 문: coins로 반복
# 시작: 잔돈보다 작은 애들 중 큰 것부터(if 문)
# 빼기 반복(조건: 뺐을 때 0과 같거나 커야함)
# for문 끝날 때마다 검사: 0인지 -> 0이면 break

for coin in coins:
  if coin > jandon:
    continue
  elif jandon==0:
    break
  while coin<=jandon:
    if jandon-coin==0:
      jandon-=coin
      cnt+=1
      break
    if jandon-coin<0:
      break
    else:
      cnt+=1
      jandon-=coin
print(cnt)