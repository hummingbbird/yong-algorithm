# https://www.acmicpc.net/problem/1197
import sys
sys.setrecursionlimit(10**6)
v, e = map(int, sys.stdin.readline().split(" "))

# 크루스칼 알고리즘으로 풀어보자
mst = []
edges = []
mst_weight=0
# 1. 간선 입력 받기
for i in range(e):
  edge = list(map(int, sys.stdin.readline().split(" ")))
  edges.append(edge)

# 2. weight 기준으로 정렬
edges.sort(key=lambda x: x[2])

# 3. cycle 확인을 위한 disjoint set 함수 생성

parent = [int(i) for i in range(v+1)]

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
    
for u, v, weight in edges:
  if find_set(u) != find_set(v):
    # mst.append((u,v))
    union_set(u, v) 
    mst_weight+=weight

print(mst_weight)   
    