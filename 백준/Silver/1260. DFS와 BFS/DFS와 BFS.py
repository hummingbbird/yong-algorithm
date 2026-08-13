import queue

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
ans_dfs = []
ans_bfs = []

for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(1, N+1):
    adj[i].sort()

# 1. dfs 함수 구현
dfs_v = [0] * (N+1)
def dfs(c):
    ans_dfs.append(c)
    dfs_v[c] = 1

    for n in adj[c]:
        if dfs_v[n] == 0:
            dfs(n)

dfs(V)
 
# 2. bfs 함수 구현
bfs_v = [0] * (N+1)
tovisit = queue.Queue()

def bfs(s):
    tovisit.put(s)

    while not tovisit.empty():
        u = tovisit.get()
        if bfs_v[u] == 1:
            continue

        bfs_v[u] = 1
        ans_bfs.append(u)

        for v in adj[u]:
            if bfs_v[v] == 0:
                tovisit.put(v)

bfs(V)

print(*ans_dfs)
print(*ans_bfs)
                
        