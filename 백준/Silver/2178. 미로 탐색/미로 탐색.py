import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 0. 초기 세팅
# 방향 리스트를 만들어둔다. (반복문을 통해 활용 예정)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
adj = []
for _ in range(N):
    adj.append(list(map(int, input().strip())))

def bfs(x, y):
    tovisit = deque([])
    tovisit.append((x, y))
    
    while tovisit:
        cur_x, cur_y = tovisit.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            # 1)범위를 벗어나지 않고, 2)갈 수 있는 길이라면
            if 0 <= nx < N and 0 <= ny < M and adj[nx][ny] == 1:
                adj[nx][ny] = adj[cur_x][cur_y] + 1
                tovisit.append((nx, ny))
    return adj[N-1][M-1]

print(bfs(0,0))