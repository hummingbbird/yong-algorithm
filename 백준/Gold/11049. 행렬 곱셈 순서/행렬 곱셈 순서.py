import math

def mcm(p):
    n = len(p)
    dp = [[math.inf] * n for _ in range(n)]
    for s in range(n - 1):
        dp[s][s + 1] = 0

    for r in range(2, n):
        for s in range(n - r):  # 시작 index
            e = s + r  # 끝 index
            for i in range(s + 1, e):
                dp[s][e] = min(dp[s][e], dp[s][i] + dp[i][e] + p[s] * p[i] * p[e])

    return dp[0][n - 1]

n = int(input())
matrix = []

for i in range(n):
    a, b = map(int, input().split())
    matrix.append(a)
    if i == n - 1:
        matrix.append(b)
print(mcm(matrix))
