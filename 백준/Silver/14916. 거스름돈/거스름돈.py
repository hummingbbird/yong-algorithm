# https://www.acmicpc.net/problem/14916
import sys
input = sys.stdin.readline
# 거스름돈이 2 or 5원만 가능
n = int(input())
cnt=0

while True:
  if n % 5 == 0:
    cnt += n // 5
    break
  else:
    n-=2
    cnt+=1
  if n < 0:
    break

if n<0:
  print(-1)
else:
  print(cnt)
