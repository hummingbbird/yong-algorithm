# https://www.acmicpc.net/problem/4354
import sys

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
  return cpi[-1]

while True:
  a=input()
  n=len(a)
  if a == ".":
    break
  maxPi = compute_pi(a)
  if len(a) % (len(a)-maxPi): # 제곱 형태가 이루어질 수 없는 경우
    print(1)
  else:
    print(len(a)//(len(a)-maxPi))
  