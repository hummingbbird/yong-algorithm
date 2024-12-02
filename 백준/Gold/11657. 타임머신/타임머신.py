# https://www.acmicpc.net/problem/11657
# 벨만포드 sssp 조건: weighted, directed, 시작노드 s, 가중치에 음수가 있어도 ok
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [sys.maxsize for _ in range(n+1)] # 최단 경로
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bellmanford(start):
    dp[start] = 0
    for i in range(1, n + 1):
        for j in range(m):
            now, next, w = graph[j][0], graph[j][1], graph[j][2]
            if dp[now] != sys.maxsize and dp[next] > dp[now] + w:
                dp[next] = dp[now] + w
                if i == n:
                    return True
    return False

hasNegative = bellmanford(1)

if hasNegative:
  print(-1)
else:
  # 음수 순환이 없으면
  for i in range(2, n+1):
    if dp[i] == sys.maxsize:
      print(-1)
    else:
      print(dp[i])
      