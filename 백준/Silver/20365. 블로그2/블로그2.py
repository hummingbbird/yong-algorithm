# https://www.acmicpc.net/problem/20365
import sys
input = sys.stdin.readline
n = int(input())
problems = input()
change = 0
for i in range(len(problems)-2):
  if problems[i] != problems[i+1]:
    change+=1

if change==0:
  print(1)
elif change%2!=0:
  print((change//2)+2)
else:
  print((change//2)+1)
  