def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        # 1. 지각 마지노선 시간 계산
        sched = schedules[i]
        hour = sched // 100
        minute = sched % 100 + 10
        if minute >= 60:
            hour += 1
            minute -= 60
        limit_time = hour * 100 + minute
        
        # 2. 출근 기록 확인
        is_success = True
        for j in range(7):
            current_day = (startday + j - 1) % 7
            
            # 토, 일은 제외
            if current_day == 5 or current_day == 6:
                continue
                
            # 지각
            if timelogs[i][j] > limit_time:
                is_success = False
                break
                
        if is_success:
            answer += 1
            
    return answer