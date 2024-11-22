# https://www.acmicpc.net/problem/4386
import sys
import math

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


# 두 점 사이의 거리를 리턴
def distance(x, y):
  answer = math.sqrt((x[1]-y[1])**2 + (x[0]-y[0])**2)
  return answer

# 1. 입력 받기
n = int(sys.stdin.readline())
coordinate = []
edges=[]
mst=[]
for _ in range(n):
  x, y = map(float, sys.stdin.readline().split(" "))
  coordinate.append((x, y))

# 2. 가중치값 저장
# for i in range(n): #i=0,1,2
#   if i==n-1:
#     a, b = i, 0
#   else:
#     a, b = i, i+1
#   # a, b = i, 0 if i==n-1 else i,i+1
#   edge=[a, b, distance(coordinate[a], coordinate[b])]
#   edges.append(edge)

for i in range(n-1):
  for j in range(i+1, n):
    edges.append([i, j, distance(coordinate[i], coordinate[j])])

# 2. weight 기준으로 정렬
edges.sort(key=lambda x: x[2])

parent = [int(i) for i in range(n+1)]
result=0

for edge in edges:
  u, v, weight = edge
  if find_set(u) != find_set(v):
    union_set(u, v)
    result+=weight

print(round(result,2))
    