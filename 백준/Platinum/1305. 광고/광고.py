# https://www.acmicpc.net/problem/1305
import sys
input = sys.stdin.readline

L = int(input())
avtm=input().strip()

def compute_pi(p):
  m = len(p)
  cpi = [0] * m
  j=0
  for i in range(1,m):
    while j>0 and p[i] != p[j]:
      j = cpi[j-1]
    if p[i]==p[j]:
      j+=1
      cpi[i]=j
  return cpi

pi = compute_pi(avtm)
answer=L-pi[-1]
print(answer)
        