import sys
input = sys.stdin.readline
t = int(input())
goal = [int(input()) for _ in range (t)]
stack = []
my_sort = []
ans = []
i=0
num = 1

while (num <= t):
    while goal[i] >= num:
        stack.append(num)
        ans.append("+")
        num+=1
    # 여기 왔다는 건 같아졌다는 것
    num-=1
    my_sort.append(stack.pop())
    ans.append("-")
    i+=1
    while len(stack)!=0 and stack[-1] == goal[i]:
        my_sort.append(stack.pop())
        ans.append("-")
        i+=1
    num+=1
    continue

if goal == my_sort:
    for i in range(len(ans)):
        print(ans[i])
else:
    print("NO")