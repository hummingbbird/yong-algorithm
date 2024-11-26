import sys

parent = []
cnt = []
p1 = {}
number = {}
def find(a):
    global parent
    if a == parent[a]:
        return a

    tmp = find(parent[a])
    parent[a] = tmp
    return parent[a]

def union(a, b):
    global parent
    global cnt
    a = find(a)
    b = find(b)
    if a != b:
        if a < b:
            parent[b] = a
            cnt[a] += cnt[b]
            return cnt[a]
        else:
            parent[a] = b
            cnt[b] += cnt[a]
            return cnt[b]
    return cnt[a]

T = int(sys.stdin.readline())
F = ""
for q in range(T):
    F = int(sys.stdin.readline())
    parent = ["" for q in range((F*2)+1)]
    cnt = [1 for i in range((F*2)+1)]
    for i in range(F*2+1):
        parent[i] = i

    dic = {}
    idx = 0

    for z in range(F):
        friend1, friend2 = map(str, sys.stdin.readline().split())
        if F == 1:
            print(2)
        else:
            if not friend1 in dic:
                idx += 1
                dic[friend1] = idx
            if not friend2 in dic:
                idx += 1
                dic[friend2] = idx
            print(union(dic[friend1], dic[friend2]))