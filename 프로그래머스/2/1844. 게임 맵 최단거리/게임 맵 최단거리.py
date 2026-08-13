from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(x, y):
        tovisit = deque([])
        tovisit.append((x, y))
        
        while tovisit:
            cx, cy = tovisit.popleft()
            
            for i in range(4):
                next_x = cx + dx[i]
                next_y = cy + dy[i]
                
                if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] == 1:
                    tovisit.append((next_x, next_y))
                    maps[next_x][next_y] = maps[cx][cy]+1
        return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1

    return bfs(0,0)