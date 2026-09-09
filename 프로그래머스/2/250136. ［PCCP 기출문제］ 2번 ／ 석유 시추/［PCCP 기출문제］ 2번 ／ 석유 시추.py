from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]
    oil_sizes = {}  # {덩어리 번호: 석유} 크기 형태로 저장
    col_to_oils = [set() for _ in range(m)]  # 각 열이 포함하는 덩어리 번호 세트
    oil_id = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                size = 0
                cols = set()

                while q:
                    r, c = q.popleft()
                    size += 1
                    cols.add(c)

                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))

                # 덩어리 정보 저장
                oil_sizes[oil_id] = size
                for c in cols:
                    col_to_oils[c].add(oil_id)
                oil_id += 1

    # 각 열마다 시추관을 꽂았을 때 얻을 수 있는 최대 석유량 계산
    max_oil = 0
    for c in range(m):
        current_oil = 0
        for oid in col_to_oils[c]:
            current_oil += oil_sizes[oid]
        max_oil = max(max_oil, current_oil)

    return max_oil