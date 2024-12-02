# https://www.acmicpc.net/problem/1786
import sys
input = sys.stdin.readline
A = input()[:-1]
P = input()[:-1]

def compute_pi(p):
  m = len(p)
  cpi = [0] * m  
  # 시간 초과를 해결하기 위한 이중 반복문 사용
  j=0
  for i in range(1,m):
    while j>0 and p[i] != p[j]:
      j = cpi[j-1]
    if p[i]==p[j]:
      j+=1
      cpi[i]=j
  return cpi

n, m = len(A), len(P)
pi=compute_pi(P)
i, j = 0, 0
cnt=0
whereP = []

# 시간 초과 해결을 위한 반복문 수정
for i in range(n):
  while j>0 and A[i]!=P[j]:
    j = pi[j-1]
  if A[i] == P[j]:
    if j == m-1:
      cnt += 1
      whereP.append(str(i-m+2))
      j=pi[j]
    else:
      j+=1

print(cnt)
print(" ".join(whereP))