T = int(input())

def getNowDirection(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if gmap[i][j] == "<" or gmap[i][j] == ">" or gmap[i][j] == "^" or gmap[i][j] == "v":
                return (i, j, gmap[i][j])

for test_case in range(1, T+1):
    H, W = map(int, input().split())
    gmap = []
    dict = {"L": "<", "R": ">", "U": "^", "D": "v"}
    dict2 = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    dict3 = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    
    for _ in range(H):
        gmap.append(list(input()))
        
    # 처음 좌표 구하기
    x, y, car = getNowDirection(gmap)
    
    N = int(input())
    cmds = list(input())
    
    for cmd in cmds:
        # 상하좌우 이동인 경우
        if cmd != "S":
            # 전차 방향 돌려놓기
            gmap[x][y] = dict[cmd]
            # dict2를 이용해 나아갈 방향 결정(dx, dy)
            dx, dy = dict2[cmd]
            if 0 <= x+dx and x+dx < H and 0 <= y+dy and y+dy < W:
                if gmap[x+dx][y+dy] == ".":
                    gmap[x+dx][y+dy] = gmap[x][y]
                    gmap[x][y] = "."
                    x, y = x+dx, y+dy
        
        # 포탄 발사인 경우   
        else:
            # gmap[x][y]에 따른 dx dy 결정
            dx, dy = dict3[gmap[x][y]]
            
            # while문으로 해당 방향으로 이동(밖으로 나갈 때까지 이동)
            now_x, now_y = x, y
            while 0 <= now_x+dx and now_x+dx < H and 0 <= now_y+dy and now_y+dy < W:
                nx = now_x+dx
                ny = now_y+dy
                if gmap[nx][ny] == "#":
                    break
                elif gmap[nx][ny] == "*":
                    gmap[nx][ny] = "."
                    break
                else:
                    now_x, now_y = now_x+dx, now_y+dy
            
    print(f"#{test_case}", end=" ")
    for item in gmap:
        print(''.join(item))

