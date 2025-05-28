# 백준 1966
# 큐
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split(" "))
    dic = []

    importance = list(map(int, input().split(" ")))
    for i in range(n):
        dic.append([i, importance[i]])
    queue = deque(dic)
    importance.sort(reverse=True)
    i = 0
    while len(queue) != 0:
        if queue[0][1] < importance[0]:
            tmp = queue.popleft()
            queue.append(tmp)
        elif queue[0][0] == m:
            print(i+1)
            break
        else:
            queue.popleft()
            importance = importance[1:]
            i+=1