# https://www.acmicpc.net/problem/11497
import sys
input = sys.stdin.readline

tmp = abs(-4) # 절대값변환 함수(내장함수임)
T = int(input())
for _ in range(T):
    n = int(input())
    wood = list(map(int, input().split()))
    wood.sort()
    minimum = []
    minimum.append(wood.pop())
    while len(wood)>1:
        tmp1 = wood.pop()
        tmp2 = wood.pop()
        minimum.insert(0,tmp1)
        minimum.append(tmp2)
    if wood:
        minimum.insert(0, wood.pop())
    # print(minimum)
    minimum.append(minimum[0]) # 맨뒤랑 맨앞도 비교하기 위해
    answer= -1
    for i in range(n):
        if abs(minimum[i+1]-minimum[i]) > answer:
            answer = abs(minimum[i+1]-minimum[i])

    print(answer)