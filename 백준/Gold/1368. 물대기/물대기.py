# https://www.acmicpc.net/problem/1368
import sys
import heapq
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n+1)]
heap = []
# disjoint set 사용을 위한 함수
def find_set(u):
  if parent[u] != u: # 루트가 아닌 경우
    parent[u] = find_set(parent[u]) # 재귀
  return parent[u]

def union_set(u, v):
  # 1. u와 v의 부모 찾기
  ur = find_set(u)
  vr = find_set(v)
  # 2. 둘의 조상이 같지 않으면 vr의 조상을 ur로 업데이트(tree를 합쳐주는 거야)
  if ur != vr: 
    parent[vr] = ur



for i in range(1, n+1):
  heapq.heappush(heap, [int(input()), 0, i])

for i in range(1, n+1):
  c = list(map(int, input().split()))
  for j in range(1, n+1):
    if i != j:
      heapq.heappush(heap, [c[j-1], i, j])

result = 0
while heap:
  w, a, b = heapq.heappop(heap)
  if find_set(a) != find_set(b):
    union_set(a, b)
    result+=w

print(result)
