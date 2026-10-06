def solution(players, m, k):
    cnt = 0
    extra = []
    
    def timer():
        nonlocal extra
        newArr = []
        for i in extra:
            if i == 1:
                continue
            else:
                newArr.append(i-1)
        extra = newArr

    for player in players:
        need, cur = player//m, len(extra)
        if need > cur:
            cnt += (need - cur)
            extra += [k for _ in range(need-cur)]   
        timer()
    return cnt