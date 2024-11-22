# https://www.acmicpc.net/problem/10216
import sys
import math
# disjoint set의 개수를 구하는 문제
T = int(sys.stdin.readline())
for _ in range(T):
  n = int(sys.stdin.readline())

  parent = [int(i) for i in range(n)]

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

  camps=[]
  for _ in range(n):
    camps.append(list(map(int, sys.stdin.readline().split(" "))))

  for i in range(n-1):
    x1, y1, r1 = camps[i]
    for j in range(i+1, n):
      x2, y2, r2 = camps[j]
      if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1+r2:
        union_set(i, j)

  cnt_group = set()
  for i in range(n):
    x = find_set(i)
    if x not in cnt_group:
      cnt_group.add(x)
  print(len(cnt_group))
    