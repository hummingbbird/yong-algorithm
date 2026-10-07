from itertools import combinations

def solution(n, q, ans):
    nums = [i for i in range(1, n+1)]
    arrs = list(combinations(nums, 5))
    answer, m = 0, len(q)
    
    for arr in arrs:
        tmp = []
        for i in range(m):
            tmp.append(len(set(q[i]) & set(arr)))
        if tmp == ans:
            answer += 1
    return answer