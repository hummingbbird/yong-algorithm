# https://www.acmicpc.net/problem/4485

import heapq
import sys
input = sys.stdin.readline

def a_star_algorithm(matrix):
    n = len(matrix)
    goal = (n - 1, n - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 휴리스틱 함수: 맨해튼 거리
    def heuristic(x, y):
        return abs(goal[0] - x) + abs(goal[1] - y)

    # 우선순위 큐 초기화
    pq = []
    heapq.heappush(pq, (matrix[0][0] + heuristic(0, 0), 0, 0, matrix[0][0]))  # (f(n), x, y, g(n))
    visited = [[False] * n for _ in range(n)]

    while pq:
        f, x, y, g = heapq.heappop(pq)

        if visited[x][y]:
            continue
        visited[x][y] = True

        # 목표 지점에 도달하면 g(n)을 반환 (최소 비용)
        if (x, y) == goal:
            return g

        # 인접 노드 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                new_g = g + matrix[nx][ny]  # 현재까지의 실제 비용
                new_f = new_g + heuristic(nx, ny)  # 총 예상 비용
                heapq.heappush(pq, (new_f, nx, ny, new_g))

    return -1  # 도달 불가능한 경우 (문제 조건상 이 경우는 없을 것)

cnt=1
while True:
    n = int(input())
    # results = []
    if n == 0: # 종료
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = a_star_algorithm(matrix)
    print(f"Problem {cnt}: {result}")
    cnt+=1

