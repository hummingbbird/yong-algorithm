import sys
sys.setrecursionlimit(10 ** 6)
    
def solution(numbers, target):
    # 이게 왜 .. dfs,bfs인 거지? 난 정말 모르겠네..
    # 왜 다 돌아야 되냐면? 무조건 모든 숫자를 다 써야돼! 그래서~ 그런가?
    # 근데 이거를 .. 끝까지 다 안 돌고 답이 나올 수 있나? 가능하지! 왜냐면 .. 아 안 되지 뒤에 무슨 숫가자 있는 줄알고 계산을 멈춰요
    
    answer = 0
    
    def dfs(idx, current_sum):
        nonlocal answer
        if idx == len(numbers):
            if current_sum == target:
                answer+=1
            return
        tmp = idx
        idx+=1
        dfs(idx, current_sum-numbers[tmp])
        dfs(idx, current_sum+numbers[tmp])
        
        
    
    dfs(0, 0)
    return answer