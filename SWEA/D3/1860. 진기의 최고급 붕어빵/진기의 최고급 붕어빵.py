from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr = deque(arr)
    used_boong = 0
    isPossible = True
    t = 0

    while arr:
        t = arr.popleft()
        # 1. 붕어빵 생
        boong = (t//M) * K
        # 2. 붕어빵 배급
        used_boong += 1

        if boong - used_boong < 0:
            isPossible = False
            break

    ans = "Possible" if isPossible else "Impossible"
    print(f"#{test_case} {ans}")
    # 기다리는 시간이 생기면 Impossible / 바로 서빙되면 Possible
