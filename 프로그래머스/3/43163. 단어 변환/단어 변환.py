from collections import deque

def canChange(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    return True if cnt == 1 else False


def solution(begin, target, words):
    words = words + [begin]
    
    # 1. 인접 리스트 형태로 변환
    adj = [[] for _ in range(len(words))]
    for i in range(len(words)):
        for j in range(len(words)):
            # if i번째 단어랑 j번째 단어랑 하나 차이가 나면 간선 연결되니까 adj에 추가
            if canChange(words[i], words[j]):
                adj[i].append(j)
    print(adj)
    
    # 2. bfs 구현
    visited= [False] * len(words)
    tovisit= deque([])
    def bfs(s):
        tovisit.append((s, 0))
        visited[s] = True
        
        while tovisit:
            vn, dist = tovisit.popleft()
            
            if words[vn] == target:
                return dist
            
            visited[vn] = True

            for n in adj[vn]:
                if not visited[n]:
                    visited[n] = True
                    tovisit.append((n, dist+1))
        return 0
                
            
    # bfs(len(words)-1) (begin 단어로 시작)
    return bfs(len(words)-1)
            
    