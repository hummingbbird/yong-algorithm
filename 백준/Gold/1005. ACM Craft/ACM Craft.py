# https://www.acmicpc.net/problem/1005
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n, k = map(int, input().split(" "))
  delay=[0]+list(map(int, input().split(" "))) # 각 node별 짓는 데 걸리는 시간
  adj = [[] for _ in range(n+1)]
  indegree = [0 for _ in range(n+1)]
  dp = [0 for _ in range(n+1)]

  # 간선 입력
  for i in range(k):
    u, v = map(int, input().split(" "))
    adj[u].append(v)
    indegree[v]+=1
    
  que = deque()
  for i in range(1, n+1):
    # in-edges가 없다면 que에 추가하고, dp값 업데이트
    if indegree[i] == 0:
      que.append(i)
      dp[i] = delay[i]

  while que:
    tmp=que.popleft()
    for i in adj[tmp]:
      indegree[i]-=1
      dp[i] = max(dp[tmp]+delay[i], dp[i])
      if indegree[i] == 0:
        que.append(i)

  w=int(input())
  print(dp[w])