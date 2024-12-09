import sys
import heapq # heapq는 min-heap임
input = sys.stdin.readline

n = int(input())
assigns = []
for _ in range(n):
  tmp = list(map(int, input().split()))
  # heapq.heappush(assigns, tmp)
  assigns.append(tmp)

assigns.sort()
possible = []
answer=0

for date in range(n, 0, -1):
  while assigns and assigns[-1][0]>=date:
    possible.append(assigns.pop()[1])
  if possible:
    possible.sort()
    answer+=possible.pop()
print(answer)