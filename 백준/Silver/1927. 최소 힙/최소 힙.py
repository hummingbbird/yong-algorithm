# 백준 11279
import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap=[]

for _ in range(n):
    x = int(input())
    if x == 0:
        print(heapq.heappop(heap) if len(heap)!=0 else 0)
    else:
        heapq.heappush(heap, x)