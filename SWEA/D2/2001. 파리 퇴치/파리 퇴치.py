T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    ans = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp = 0
            for k in range(m):
                tmp += sum(arr[i+k][j:j+m])
            ans = max(ans, tmp)

    print(f"#{test_case} {ans}")