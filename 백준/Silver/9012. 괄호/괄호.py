# 백준 9012
# 스택
import sys
input = sys.stdin.readline

def validVPS(ps):
    stack = []
    for s in ps:
        if s=="(":
            stack.append("(")
        elif len(stack) == 0:
            stack.append(")")
        elif stack[-1]=="(":
            stack.pop()
    print("YES" if len(stack)==0 else "NO")

t = int(input())

for _ in range(t):
    validVPS(input()[:-1])