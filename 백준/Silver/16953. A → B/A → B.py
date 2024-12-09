# https://www.acmicpc.net/problem/16953
import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 0
# 2곱하기 or 뒤에 1붙이기(10배하고+1하기와 같음)
while(b!=a):
    cnt+=1
    temp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if temp == b:
        print(-1)
        break
else:
    print(cnt+1)
