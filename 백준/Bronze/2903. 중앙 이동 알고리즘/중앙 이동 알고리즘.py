n = int(input())
#재귀를 써야하는 것인가?
def jae(n):
    if n==0:
        return 2
    else:
        return (2*jae(n-1)) - 1

print(jae(n)**2)
