N = int(input())
tp = []
for _ in range(N):
    tp.append(list(map(int, input().split())))

# 방법1: 완전 탐색(dfs)
def dfs(n, sm):
    global ans
    # 1. 종료 조건
    if n >= N:
        ans = max(ans, sm)
        return
    # 2. 하부 호출 
    # case1) 상담하는 경우
    if n + tp[n][0] <= N:
        dfs(n+tp[n][0], sm+tp[n][1])
    # case2) 상담 안 하는 경우
    dfs(n+1, sm)

ans = 0
dfs(0,0)
print(ans)

# 방법2: dp
dp = [0 for _ in range(N+1)]
for n in range(N-1, -1, -1):
    if n + tp[n][0] > N:
        dp[n] = dp[n+1]
    else:
        dp[n] = max(dp[n+1], tp[n][1]+dp[n+tp[n][0]])
# print(dp[0])