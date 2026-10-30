# points:운송 포인트 / routes: 로봇 x대의 운송 경로
def solution(points, routes):
    points = [[0,0]] + points
    r_max, c_max = max(map(lambda x:x[0], points)), max(map(lambda x:x[1], points)) 
    dic={}
    n = len(points)
    x = len(routes) # 로봇 개수
    m = len(routes[0]) # 루트의 길이
    
    # 일단 routes에 있는 아이들의 이동은 한 번에 이동 1번씩
    for j in range(x): # 로봇 개수 만큼 반복
        time = 0
        cur_xy = list(points[routes[j][0]])
        if (cur_xy[0], cur_xy[1],time) in dic.keys():
            dic[(cur_xy[0], cur_xy[1],time)] += 1
        else:
            dic[(cur_xy[0], cur_xy[1],time)] = 1
            
        for i in range(m-1): # 경로 만큼 반복
            next_xy = list(points[routes[j][i+1]])
            
            while cur_xy != next_xy:
                # r좌표부터
                if cur_xy[0] != next_xy[0]:
                    if cur_xy[0] > next_xy[0]:
                        cur_xy[0] -= 1
                    else:
                        cur_xy[0] += 1
                # 다음 c좌표
                elif cur_xy[1] != next_xy[1]:
                    if cur_xy[1] > next_xy[1]:
                        cur_xy[1] -= 1
                    else:
                        cur_xy[1] += 1
                time += 1  
                if (cur_xy[0], cur_xy[1],time) in dic.keys():
                    dic[(cur_xy[0], cur_xy[1],time)] += 1
                else:
                    dic[(cur_xy[0], cur_xy[1],time)] = 1
    answer = 0
    for item in dic:
        if dic[item] != 1:
            answer+=1
            
    return answer