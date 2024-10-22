# https://www.acmicpc.net/problem/2751
import sys
N = int(sys.stdin.readline())

# 1. 개수 count(1~10**6)
minus = [0 for _ in range(1, (10**6)+2)]
numbers = [0 for _ in range(1, (10**6)+2)]

for _ in range(N):
  n = int(sys.stdin.readline())
  if n < 0:
    minus[n*-1]+=1
  else:
    numbers[n]+=1

# 2. 누적합 구할....... 필요가 없슈, 어차피 하나씩있는데
for i in range(len(minus)-1, -1, -1):
  if minus[i] != 0:
    print(i*-1)

for i in range(len(numbers)):
  if numbers[i] != 0:
    print(i)
