# https://www.acmicpc.net/problem/13418
# 골드3 - 학교 탐방하기
import sys

input=sys.stdin.readline
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

n, m = map(int, input().split())
paths=[]
tired_default=0
for _ in range(m+1):
  tmp = list(map(int, input().split()))
  if tmp[0]==0 or tmp[1] == 0:
    if tmp[2] == 0:
      tired_default=1
    continue
  paths.append(tmp)

# # 1. 최악의 경로: 0을 많이 지나야함
# parent = [int(i) for i in range(n+1)]
# paths.sort(key=lambda x:x[2])
# # print(paths)
# tired=tired_default
# for a, b, w in paths:
#   if find_set(a) != find_set(b):
#     union_set(a, b)
#     if w == 0:
#       tired+=1
# tired_worst = pow(tired, 2)
# # 2. 최고의 경로: 1을 많이 지나야함
# parent = [int(i) for i in range(n+1)]
# paths.sort(key=lambda x:x[2], reverse=True)

# tired=tired_default
# for a, b, w in paths:
#   if find_set(a) != find_set(b):
#     union_set(a, b)
#     if w == 0:
#       tired+=1
# tired_best = pow(tired, 2)

# print(tired_worst-tired_best)

def calc_path(reverse):
  global parent
  parent = [int(i) for i in range(n+1)]
  paths.sort(key=lambda x:x[2], reverse=reverse)

  tired=tired_default
  for a, b, w in paths:
    if find_set(a) != find_set(b):
      union_set(a, b)
      if w == 0:
        tired+=1
  return tired**2

print(calc_path(False)-calc_path(True))