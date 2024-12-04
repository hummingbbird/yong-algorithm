# https://www.acmicpc.net/problem/2212
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors=sorted(list(map(int, input().split())))
# print(sensors)

if k >= n:
  print(0)
else:
  dist=[]
  for i in range(1, len(sensors)):
    dist.append(sensors[i]-sensors[i-1])
  dist.sort(reverse=True)
  print(sum(dist[k-1:]))