# 백준 10828
import sys
input = sys.stdin.readline

t = int(input())
i = 0
stack = []
while i<t:
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        print(stack.pop() if len(stack)!=0 else -1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if len(stack)==0 else 0)
    elif len(stack)!= 0:
        print(stack[-1])
    else:
        print(-1)
    i+=1 