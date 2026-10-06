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
        return

    for i in range(len(players)):
        need, cur = players[i]//m, len(extra)
        if need > cur:
            print(i, "번째에서", need-cur, "번 만큼 증식")
            cnt += (need - cur)
            extra += [k for _ in range(need-cur)]   
        timer()
    # timer()
    return cnt