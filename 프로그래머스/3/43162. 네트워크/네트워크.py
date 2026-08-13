def solution(n, computers):
    answer = 0
    adj = [[] for _ in range(n+1)]
    
    # adj 형식으로 세팅
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                adj[i+1].append(j+1)
    
    visited = [False] * (n+1)
    
    def dfs(c):
        visited[c] = True
        for node in adj[c]:
            if not visited[node]:
                dfs(node)
    
    for i in range(1, n+1):
        if visited[i] == False:
            answer += 1
            dfs(i)
    return answer