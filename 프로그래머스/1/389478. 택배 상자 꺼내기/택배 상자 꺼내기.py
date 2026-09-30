def solution(n, w, num):
    if w == 1:
        return n-num+1
    
    ans = []
    h = (n//w) if n%w == 0 else (n//w) + 1
    boxes = [[0] * w for _ in range(h)] 
    
    dx, dy = 0, 0
    y_yeonsan = 1
    target = 0
    
    # 1. 2차원 배열에 삽입
    for i in range(1, n+1):
        boxes[dx][dy] = i
        
        if i == num:
            target = dy
        
        if i % w == 0:
            dx += 1
            if dy > 0:
                dy -= w
                y_yeonsan = -1
            else:
                dy += w
                y_yeonsan = 1
        else:
            dy += y_yeonsan  

    for i in range(h):
        if boxes[i][target] >= num:
            ans.append(boxes[i][target])
            
    return len(ans)