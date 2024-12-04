# https://www.acmicpc.net/problem/20300
import sys
input = sys.stdin.readline

n = int(input())
equips = list(map(int, input().split()))
equips.sort()


# 짝수일 경우, 최대인 아이는 무조건 최소와 더해져야만 m의 크기를 최대한 줄일 수 있어
if n%2==0:
  m = -1
  for i in range((n//2)):
    tmp = equips[i] + equips[n-i-1]
    if tmp > m:
      m = tmp
else:
  m = equips.pop()
  for i in range((n//2)):
    tmp = equips[i] + equips[n-i-2]
    if tmp > m:
      m = tmp
  
print(m)
  

