def strToArr(target):
    return [int(target[:2]), int(target[3:])]

def arrToInt(target):
    return (target[0] * 100) + target[1]

def arrToStr(target):
    answer = "0" if target[0] < 10 else ""
    answer += str(target[0])
    
    answer += ":"
    
    ss = target[1]
    answer += "0" if target[1] < 10 else ""
    answer += str(target[1])
    
    return answer

def processCommand(cmd, ctime, video_len, op_start, op_end):
        # ctime = [mm, ss]의 형태
        
        # 오프닝 구간인 경우 오프닝이 끝나는 위치로 이동
        if arrToInt(strToArr(op_start)) <= arrToInt(ctime) <= arrToInt(strToArr(op_end)):
            ctime = strToArr(op_end)
            
        if cmd == "prev":
            if ctime[0] == 0 and ctime[1] < 10:
                ctime = [0, 0]
            elif ctime[1] < 10:
                ctime[0] -= 1
                ctime[1] += 50
            else:
                ctime[1] -= 10
        elif cmd == "next":
            if ctime[1] >= 50:
                ctime[0] += 1
                ctime[1] -= 50
            else:
                ctime[1] += 10
            
        # video_len보다 크면 video_len으로 변경
        if arrToInt(ctime) > arrToInt(strToArr(video_len)) :
            ctime = strToArr(video_len)
        
        # 오프닝 구간인 경우 오프닝이 끝나는 위치로 이동
        if arrToInt(strToArr(op_start)) <= arrToInt(ctime) <= arrToInt(strToArr(op_end)):
            ctime = strToArr(op_end)
            
        return ctime
    
def solution(video_len, pos, op_start, op_end, commands):
    time = strToArr(pos)
    
    for cmd in commands:
        time = processCommand(cmd, time, video_len, op_start, op_end)
    return arrToStr(time)