n = int(input())
xs=[]
ys=[]
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
xs = sorted(xs)
ys = sorted(ys)
if n==1:
    print(0)
else:
    print((xs[-1]-xs[0])*(ys[-1]-ys[0]))