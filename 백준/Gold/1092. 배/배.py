# https://www.acmicpc.net/problem/1092
# 골드5 - 배
import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt=0
if max(cranes) < max(boxes):
  cnt = -1
else:
  while boxes:
    for c in cranes:
      if boxes and c < boxes[-1]:
        continue
      for b in boxes:
        if c >= b:
          boxes.remove(b)
          break
    cnt+=1
    
    
print(cnt)
