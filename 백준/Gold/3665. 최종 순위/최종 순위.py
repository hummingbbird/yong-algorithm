# https://www.acmicpc.net/problem/3665
import sys
import heapq
input = sys.stdin.readline

T = int(input())

def final_rank():
  n = int(input()) # node 수
  last_rank = list(map(int, input().split(" ")))

  adj=[[] for _ in range(n+1)]
  d=[0]*(n+1)

  # 주어진 순위대로 adj에 edge 정보 추가
  lose_nodes=[i for i in range(1, n+1)]
  for win in last_rank:
    if win==0:
      continue
    lose_nodes.remove(win)
    for lose in lose_nodes:
      adj[win].append(lose)
      d[lose]+=1
      
  m = int(input()) # edge 정보 개수      
  # case2: m=0일 경우 순위 변동 없이 그대로 출력
  if m==0:
    return " ".join(map(str, last_rank))
  last_rank.insert(0,0)
  # 바뀐 순위 정보 업데이트
  for _ in range(m):
    a, b = map(int, input().split(" "))
    if b in adj[a]:
      adj[a].remove(b)
      adj[b].append(a)
      d[a]+=1
      d[b]-=1
    else:
      adj[b].remove(a)
      adj[a].append(b)
      d[b]+=1
      d[a]-=1

  S=[]
  for i in range(1, n+1):
    if d[i] == 0:
      heapq.heappush(S, i)
      
  result = []
  while S:
    tmp = heapq.heappop(S)
    result.append(tmp)
    for v in adj[tmp]:
      d[v]-=1
      if d[v] == 0:
        heapq.heappush(S, v)
  
  hastrue = False
  for dv in d:
      if dv:
          hastrue = True
          break

  if hastrue:
      return "IMPOSSIBLE"
  else:
      return " ".join(map(str, result))
  

for _ in range(T):
  print(final_rank())
