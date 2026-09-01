def solution(bandage, health, attacks):
    answer = 0
    t, x, y = bandage
    max_health = health
    cnt, sequence = 1, 0
    attacks.sort(key = lambda x: -x[0])
    n_attack = attacks.pop()
    last_attack = attacks[0][0]
    
    while True:
        # 공격 시간인 경우
        if n_attack[0] == cnt:
            health -= n_attack[1]
            sequence = 0
            if health <= 0:
                return -1
            
            if attacks == []:
                break
            n_attack = attacks.pop()
        
        # 공격 시간이 아닌 경우
        else:
            health += x
            sequence += 1
            
            if sequence == t:
                health += y
                sequence = 0
                
            if health > max_health:
                health = max_health
        
        cnt += 1
            
    return health