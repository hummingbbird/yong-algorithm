from collections import deque

def solution(bandage, health, attacks):
    # attack은 공격시간 기준 오름차순이라 걍..반복하면됨
    [t, x, y] = bandage
    attack_timing = deque(attacks)

    time = attacks[-1][0]
    yeonsok = 0
    cur_health = health
    
    for i in range(1, time+1):
        # 몬스터 공격이 있다면 그걸 해야함.
        if attack_timing[0][0] == i:
            [timing, power] = attack_timing.popleft()
            cur_health -= power
            yeonsok = 0
            if cur_health <= 0:
                return -1
        # 기본으로 해야할 일
        else:
            cur_health = min(health, cur_health+x)
            yeonsok += 1
            
            if yeonsok == t:
                cur_health = min(health, cur_health+y)
                yeonsok = 0
    return cur_health