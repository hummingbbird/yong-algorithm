def solution(info, n, m):
    # dp 딕셔너리: { a_sum (도둑 A의 누적 흔적): b_sum (도둑 B의 누적 흔적 최솟값) }
    dp = {}
    
    # 1. 첫 번째 물건 처리
    first_a, first_b = info[0]
    
    # 첫 물건을 A가 훔치는 경우
    if first_a < n:
        dp[first_a] = 0
    
    # 첫 물건을 B가 훔치는 경우
    if first_b < m:
        if 0 in dp:
            dp[0] = min(dp[0], first_b)
        else:
            dp[0] = first_b
            
    # 첫 물건부터 둘 다 한계치를 넘으면 불가능
    if not dp:
        return -1
        
    # 2. 두 번째 물건부터 끝까지 반복
    for i in range(1, len(info)):
        item_a, item_b = info[i]
        next_dp = {}
        
        for a_sum, b_sum in dp.items():
            # [경우 1] 이번 물건을 A에게 주는 경우
            if a_sum + item_a < n:
                next_a = a_sum + item_a
                next_b = b_sum
                # 1. 다음 dp에 next_a가 없거나 2. 이미 있는데 그 값보다 next_b가 작은 경우 -> next에 추가
                if next_a not in next_dp or next_dp[next_a] > next_b:
                    next_dp[next_a] = next_b
                    
            # [경우 2] 이번 물건을 B에게 주는 경우(동일)
            if b_sum + item_b < m:
                next_a = a_sum
                next_b = b_sum + item_b
                if next_a not in next_dp or next_dp[next_a] > next_b:
                    next_dp[next_a] = next_b
        # dp 갱신            
        dp = next_dp
        # 만약 갈 수 있는 유효한 상태가 하나도 없다면 종료
        if not dp:
            return -1
            
    # 3. dp의 a_sum(key) 중 최솟값 반환
    return min(dp.keys()) if dp else -1