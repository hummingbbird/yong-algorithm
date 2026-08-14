def isPrime(num):
    if num < 2:
        return False
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    s = set([])
    
    visited = [False] * len(numbers)
    
    def dfs(c, idx):
        s.add(int(c))
        visited[idx] = True
        for i in range(len(numbers)):
            if visited[i] == False:
                dfs(c+numbers[i], i)
        visited[idx] = False
    
    for i in range(len(numbers)):
        dfs(numbers[i], i)
    
    for n in s:
        if isPrime(n):
            answer += 1
    
    return answer