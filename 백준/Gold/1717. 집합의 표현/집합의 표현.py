import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split(" "))

def find_set(u):
  if parent[u] != u: # 루트인 경우
    parent[u] = find_set(parent[u])
  return parent[u]

def union(u, v):
  ur = find_set(u)
  vr = find_set(v)
  if ur!=vr:
    parent[vr]=ur

parent = list(range(n+1))

for line in sys.stdin:
  op, u, v = map(int, line.split())
  if op==0:
    union(u, v)
  else:
    if find_set(u) == find_set(v):
      print("YES")
    else:
      print("NO")