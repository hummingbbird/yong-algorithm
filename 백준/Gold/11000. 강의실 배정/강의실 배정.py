# https://www.acmicpc.net/problem/11000
# 골드5 - 강의실 배정
import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    classes.append(list(map(int,input().split(' '))))
classes.sort(key=lambda x : (x[0],x[1]))

heap = [classes[0][1]] # 가장 첫 회의가 끝나는 시간 저장
for i in range(1, n):
    # 앞 수업이 끝난 후 다음 수업이 시작되면(정상적인 경우)
    if heap[0] <= classes[i][0]:
        heapq.heappop(heap)
    # 다음 수업 끝나는 시간 저장
    heapq.heappush(heap, classes[i][1])

print(len(heap))

