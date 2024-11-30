# https://www.acmicpc.net/problem/1738
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [-sys.maxsize for _ in range(n+1)] # 최단 경로
route=[0 for i in range(n+1)] # 이전 경로?
graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bellmanford(start):
    dp[start] = 0
    
    for i in range(n):
        for j in range(m):
            now, next, cost = graph[j][0], graph[j][1], graph[j][2]
            if dp[now] != -sys.maxsize and dp[next] < dp[now] + cost:
                dp[next] = dp[now] + cost
                route[next] = now
                if i == n-1:
                  dp[next] = sys.maxsize


bellmanford(1)
answer=[n]
# print(dp)
if dp[n] != sys.maxsize:
  node=n
  
  while node != 1:
    node = route[node]
    answer.append(node)
  
  answer.reverse()
  print(*answer)
else:
  print(-1)