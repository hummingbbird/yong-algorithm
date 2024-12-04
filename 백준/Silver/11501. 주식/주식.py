# https://www.acmicpc.net/problem/11501
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  stocks = list(map(int, input().split()))
  answer=0
  maxPrice=0

  for i in range(n-1, -1, -1):
    if stocks[i] > maxPrice:
      maxPrice=stocks[i]
    else:
      answer+=maxPrice-stocks[i]

  print(answer)