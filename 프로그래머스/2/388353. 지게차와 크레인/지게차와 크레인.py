from collections import deque

# bfs를 사용한 지게차 구현
def jigecha(con, req):
    n, m = len(con), len(con[0])
    # 1. 0으로 감싸기
    for i in range(n):
        con[i] = ["0"] + list(con[i]) + ["0"] 
    con.insert(0, ["0"] * (m + 2))
    con.append(["0"] * (m + 2))
    
    
    n, m = len(con), len(con[0])
    # 2. visited(공기 닿아 있는지 리스트) 준비
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([])
    
    # 3. 테두리 True로 변경 후 queue에 담기
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                visited[i][j] = True
                queue.append((i, j))
    
    # 4. visited 완성하기
    while queue:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and con[nx][ny] == "0":
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    # 5. 완성한 visited 기반으로 뽑기 작업 진행
    change = []
    for i in range(1, n):
        for j in range(1, m):
            if con[i][j] == req and (visited[i-1][j] or visited[i+1][j] or visited[i][j-1] or visited[i][j+1]):
                change.append((i, j))
                
    # 6. 마무리 (0으로 변환 후 테두리 없애고 return)
    for c in change:
        x, y = c
        con[x][y] = "0"
    con.pop()
    con.pop(0)
    for i in range(len(con)):
        con[i] = con[i][1:-1]
    
    return con

def crain(con, req): 
    n, m = len(con), len(con[0])
    
    # 1.문자열 -> 리스트 타입으로 변경
    for i in range(n):
        con[i] = list(con[i])
        
    # 2. 다 뽑아부러
    for i in range(n):
        for j in range(m):
            if con[i][j] == req:
                con[i][j] = "0"
    return con
                
def solution(storage, requests):
    # 1. 명령어 실행
    for req in requests:
        # case1: 지게차
        if len(req) == 1:
            storage = jigecha(storage, req)
        # case2: 크레인
        else: 
            storage = crain(storage, req[0])

    # 2. 남은 컨테이너 수 return
    n, m = len(storage), len(storage[0])
    answer = 0

    for i in range(n):
        for j in range(m):
            if storage[i][j] != "0":
                answer += 1

    return answer