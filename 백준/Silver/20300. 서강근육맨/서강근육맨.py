import sys
input = sys.stdin.readline

n = int(input())
equips = list(map(int, input().split()))
equips.sort()

if n%2==0:
  m=-1
else:
  m=equips.pop()
  n-=1

for i in range(len(equips)//2):
  tmp = equips[i] + equips[n-i-1]
  if tmp > m:
    m = tmp

print(m)