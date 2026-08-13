import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 0. 초기 세팅
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 1. dfs or bfs 편한 걸루 -> dfs로 간다.
visited = [False] * (N+1) # 시간 복잡도를 고려하여 불리언 배열 형태로 작성
def dfs(c):
    visited[c] = True
    for n in adj[c]:
        if visited[n]:
            continue
        dfs(n)

ans = 0
for m in range(1, N+1):
    if not visited[m]:
       ans += 1
       dfs(m)

print(ans) 