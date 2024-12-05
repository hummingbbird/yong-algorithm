import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
# 순서 바뀌면 안 됨. 
# n=1 or n=2 -> sum(cards[0])
if n==1 or n==2:
  print(sum(cards))
else:
  cards.sort()
  bestCard = cards.pop()
  print((bestCard*(n-1))+sum(cards))