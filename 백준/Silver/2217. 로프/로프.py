# https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline

n = int(input())
ropes=[]
for _ in range(n):
  ropes.append(int(input()))
  
ropes.sort()
maxR=0
for i in range(n):
  tmp = ropes[i] * (n-i)
  if maxR < tmp:
    maxR = tmp
    
print(maxR)