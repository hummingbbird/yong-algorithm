# https://www.acmicpc.net/problem/11585
import sys
input = sys.stdin.readline

n = int(input())
wannabe = list(map(str, input().split()))
now_r = list(map(str, input().split()))
now_r += now_r[:-1]
  
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

def KMP(A, P):
  n, m = len(A), len(P)
  i, j = 0, 0
  cnt=0

  while i < n:
    if A[i] == P[j]:
      i+=1
      j+=1
    else:
      if j == 0:
        i+=1
      else:
        j=pi[j-1]
    
    if j==m:
      cnt+=1
      j=pi[j-1]
  return cnt

pi = compute_pi(wannabe)
menu_cnt = KMP(now_r, wannabe)

for i in range(menu_cnt, 0, -1):
  if menu_cnt % 1 == 0 and n%i==0:
    print(f"{menu_cnt//i}/{n//i}")
    break
  else: 
    print(f"1/{n}")


  