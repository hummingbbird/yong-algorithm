N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
	T[i], P[i] = map(int, input().split())
    

def dfs(n, sm):
    global ans
    # 1. 종료 조건: n이 N 이상인 경우
    if n >= N:
        ans = max(ans, sm)
        return
        
    # 2. 하부 호출 
    # case1) 상담하는 경우
    if n + T[n] <= N: # 날짜가 넘치지 않는 경우에만 상담 가능
        dfs(n+T[n], sm+P[n])
        
    # case2) 상담 안 하는 경우: n만 1만큼 전진(총 이익 sm은 그대로)
    dfs(n+1, sm)

ans = 0
dfs(0,0)
print(ans)