# https://www.acmicpc.net/problem/1774

import sys
import math

coordi = []
mst = []
n, m = map(int, sys.stdin.readline().split(" ")) # 4, 1
for _ in range(n):
  coordi.append(list(map(int, sys.stdin.readline().split(" "))))
  

# 2. (a, b, 가중치)가 담긴 edges 리스트 만들기
def distance(x, y):
  answer = math.sqrt((x[1]-y[1])**2 + (x[0]-y[0])**2)
  return answer
edges=[]

for i in range(n-1):
  for j in range(i+1, n):
    edges.append([i, j, distance(coordi[i], coordi[j])])
    
# print(edges)
edges.sort(key=lambda x:x[2])

# 3. mst를 이용해 최소 동선 구하기
def find_set(u):
  if parent[u] != u: # 루트가 아닌 경우
    parent[u] = find_set(parent[u]) # 재귀
  return parent[u]

def union_set(u, v):
  # u와 v의 부모 찾기
  ur = find_set(u)
  vr = find_set(v)
  # 둘의 조상이 같지 않으면 vr의 조상을 ur로 업데이트(tree를 합쳐주는 거야)
  if ur != vr: 
    parent[vr] = ur


# 이미 연결된 애들 정보 담기
parent = [int(i) for i in range(n+1)]
for _ in range(m):
  g1, g2 = map(int, sys.stdin.readline().split(" "))
  g1, g2 = g1-1, g2-1
  mst.append((g1, g2))
  union_set(g1, g2)

# 답 구하기
result=0
for u, v, weight in edges:
  if find_set(u) != find_set(v):
    mst.append((u,v))
    union_set(u, v) 
    result+=weight

# print(round(result,2))
print(format(result,".2f"))