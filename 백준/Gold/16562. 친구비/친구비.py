# https://www.acmicpc.net/problem/16562
import sys
sys.setrecursionlimit(10**6)

def find_set(u):
  if parent[u] != u:
    parent[u] = find_set(parent[u])
  return parent[u]

def union(u, v):
  ur = find_set(u)
  vr = find_set(v)
  if ur != vr:
    if ur<vr:
      parent[vr] = ur
    else:
      parent[ur] = vr
  
n, m, k = map(int, sys.stdin.readline().split(" "))
costs = list(map(int, sys.stdin.readline().split(" ")))
parent = [int(i) for i in range(n)]

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split(" "))
  a, b = a-1, b-1
  if a==b:
    continue
  union(a,b) if b>a else union(b,a)
  
for i in range(n):
  parent[i] = find_set(parent[i])
# 2. 친구비 최솟값 구하기
group = set(parent)
result=0
for i in group: # 0, 3
  min_cost=10001
  for j in range(len(parent)): # j=0~4
    if i == parent[j] and costs[j] < min_cost:
      min_cost=costs[j]
  result+=min_cost
  
print(result if result<=k else "Oh no")
      
