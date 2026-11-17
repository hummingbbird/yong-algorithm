T = int(input())
for test_case in range(1, T + 1):
    n, K = map(int, input().split())
    ans = 0
    # 1. 탐색을 위한 배열 생성
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    # 2. 가로 탐색부터
    for i in range(n):
        cnt = 0
        tmp = 0
        for j in range(n):
            if arr[i][j] == 1:
                tmp += 1
                if j == n-1 and tmp == K:
                    ans += 1
            else:
                if tmp == K:
                    ans += 1
                tmp = 0
                
      # 3. 세로 탐색
        ans2 = 0
        tmp2 = []
        for j in range(n):
            cnt = 0
            tmp = 0
            for i in range(n):
                if arr[i][j] == 1:
                    tmp += 1
                    if i == n-1 and tmp == K:
                        ans2 += 1
                        tmp2.append((i, j))
                else:
                    if tmp == K:
                        ans2 += 1
                        tmp2.append((i, j))
                    tmp = 0
	
    print(f"#{test_case} {ans + ans2}")
    #print(ans)     
    
    
