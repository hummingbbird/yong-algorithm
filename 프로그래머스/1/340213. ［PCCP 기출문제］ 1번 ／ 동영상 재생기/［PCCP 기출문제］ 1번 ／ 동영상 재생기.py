def minToSec(time):
    return (int(time[:2]) * 60) + int(time[3:])

def secToMin(time):
    mm = str(time//60)
    mm = ("0" + str(time//60)) if time//60 < 10 else str(time//60)
    ss = ("0" + str(time%60)) if time%60 < 10 else str(time%60)
    return mm + ":" + ss

def processCommand(cmd, pos, video_len, op_start, op_end):
        if cmd == "prev":
            if pos-10 < 10:
                pos = 0
            else:
                pos -= 10
                
        elif cmd == "next":
            if pos+10 > video_len:
                pos = video_len
            else:
                pos += 10
        
        if op_start <= pos <= op_end:
            pos = op_end
        
        return pos
    
def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = minToSec(video_len), minToSec(pos), minToSec(op_start), minToSec(op_end)
    
    if op_start <= pos <= op_end:
            pos = op_end
            
    for cmd in commands:
        pos = processCommand(cmd, pos, video_len, op_start, op_end)
        
    return secToMin(pos)
