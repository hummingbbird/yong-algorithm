# https://www.acmicpc.net/problem/1374
import sys
import heapq
input = sys.stdin.readline

times = []
n = int(input())

for i in range(n):
  time = list(map(int, input().split()))
  times.append([time[1], time[2]])
times.sort(key=lambda x : (x[0],x[1]))

heap = [times[0][1]] # 가장 첫 회의가 끝나는 시간 저장
for i in range(1, n):
    # 앞 수업이 끝난 후 다음 수업이 시작되면(정상적인 경우)
    if heap[0] <= times[i][0]:
        heapq.heappop(heap)
    # 다음 수업 끝나는 시간 저장
    heapq.heappush(heap, times[i][1])
print(len(heap))