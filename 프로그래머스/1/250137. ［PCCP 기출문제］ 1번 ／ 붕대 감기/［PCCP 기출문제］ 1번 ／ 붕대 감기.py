def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    cnt, sequence = 1, 0
    attack_idx = 0
    
    while attack_idx < len(attacks):
        n_attack = attacks[attack_idx]
        
        # 공격 시간인 경우
        if n_attack[0] == cnt:
            health -= n_attack[1]
            sequence = 0
            # 체력이 0보다 작아진 경우
            if health <= 0:
                return -1
            attack_idx += 1
        
        # 공격 시간이 아닌 경우
        else:
            health += x
            sequence += 1
            
            # 연속 성공일 경우
            if sequence == t:
                health += y
                sequence = 0
            
            # 최대 체력 이상을 가지려고 할 때
            if health > max_health:
                health = max_health
        
        cnt += 1
            
    return health
