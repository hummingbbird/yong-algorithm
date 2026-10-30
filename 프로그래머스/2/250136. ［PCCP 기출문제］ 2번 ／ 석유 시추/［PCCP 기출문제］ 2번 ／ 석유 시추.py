from collections import deque
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    m_area = [0] * m
    def bfs(x, y):
        area = 1
        tovisit = deque([])
        tovisit.append((x, y))
        visited[x][y] = True
        m_range = [y]
        
        while tovisit:
            cur_x, cur_y = tovisit.popleft()
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    tovisit.append((nx, ny))
                    m_range.append(ny)
                    area += 1
        for idx in set(m_range):
            m_area[idx] += area
        # print(f"area: {area}, m_range: {set(m_range)}")
        
        # return area
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and land[i][j] == 1:
                bfs(i, j)
            else:
                visited[i][j] = True
    return max(m_area)