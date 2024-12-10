# https://www.acmicpc.net/problem/10423
# 골드3 - 전기가 부족해
import sys
input = sys.stdin.readline

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

def find_station(u):
  r = u
  while r != parent[r]:
    if parent[r] in station:
      return parent[r]
    r = parent[r]
  return u

n, m, k = map(int, input().split())
station = list(map(int, input().split()))

parent = [0] * (n+1)
for i in range(1, n+1):
  # 발전소가 있으면 parent==0으로 지정
  if i in station:
    parent[i] = 0
  else:
    parent[i] = i

cables = []
for _ in range(m):
  cable = list(map(int, input().split()))
  cables.append(cable)

# 2. 간선 weight 기준으로 정렬
cables.sort(key=lambda x:x[2])

cost = 0
for a, b, w in cables:
  if find_set(a) != find_set(b):
    union_set(a, b)
    cost+=w
print(cost)