t = int(input())
gsr = [25, 10, 5, 1]
for _ in range(t):
    ans = []
    c = int(input())
    for i in range(4):
        ans.append(str(c//gsr[i]))
        c = c%gsr[i]

    print(' '.join(ans))
