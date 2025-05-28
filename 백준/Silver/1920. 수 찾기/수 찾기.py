# 백준 1920
import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split(" ")))
m = int(input())
guess = list(map(int, input().split(" ")))

for g in guess:
    if g in A:
        print(1)
    else:
        print(0)
