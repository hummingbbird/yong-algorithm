def solution(n, lost, reserve):
    answer = n
    reserve.sort()
    # 여벌 옷 도난당한 칭긔 선처리하기
    after_lost = list(set(lost)-set(reserve))
    after_reserve = list(set(reserve)-set(lost))

    for r in after_reserve:
        candi1, candi2 = r-1, r+1
        if candi1 in after_lost:
            after_lost.remove(candi1)
        elif candi2 in after_lost:
            after_lost.remove(candi2)
    return answer - len(after_lost)