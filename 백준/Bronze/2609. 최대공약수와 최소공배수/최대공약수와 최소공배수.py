#1.최대공약수 구하는 함수
def GCD(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i==0 and b%i==0:
            return i

n, m = map(int, input().split())
gcd = GCD(n, m)
print(gcd)
print(gcd * (n//gcd) * (m//gcd))