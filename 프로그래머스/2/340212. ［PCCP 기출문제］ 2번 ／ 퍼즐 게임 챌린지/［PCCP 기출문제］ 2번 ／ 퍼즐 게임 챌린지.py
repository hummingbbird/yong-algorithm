def isPossible(diffs, times, limit, level):
    for i in range(len(diffs)):
        diff, time_cur = diffs[i], times[i]
        if diff <= level:
            limit -= time_cur
        else:
            limit -= (diff-level) * (time_cur + times[i-1]) + time_cur 
        if limit < 0:
            return False
    return True

def solution(diffs, times, limit):
    s, e = 1, max(diffs)+1
    answer = 0
    while s <= e:   
        mid = (s+e) // 2 
        if isPossible(diffs, times, limit, mid):
            answer = mid
            e = mid-1
        else:
            s = mid+1
    return answer