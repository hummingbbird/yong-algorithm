# https://www.acmicpc.net/problem/2887
# 행성 터널 민혁이 왕국 3차원 터널 최소 비용
import sys
import copy
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

n = int(input())
parent = [i for i in range(n)]

xlist, ylist, zlist = [], [], []
for i in range(n):
  x, y, z = map(int, input().split())
  xlist.append((x, i))
  ylist.append((y, i))
  zlist.append((z, i))

xlist.sort()
ylist.sort()
zlist.sort()

# 간선 구성
# edge = (가중치, a행성, b행성)
edges = []
for curList in xlist, ylist, zlist:
  for i in range(1, n):
    w1, a = curList[i-1]
    w2, b = curList[i]
    edges.append((abs(w1-w2), a, b))
        

edges.sort()


result = 0
for w, a, b  in edges:
  if find_set(a) != find_set(b): # 사이클이 생기지 않았다면
    union_set(a, b) # 두개의 행성 잇고
    result += w # 최종 가중치 합계에 해당 가중치 포함


print(result)