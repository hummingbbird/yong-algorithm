#피보나치: 재귀의 대표주자
#기본 원리: 앞 2개의 합
n = int(input())  
# def fibo(n):
#   if n==0 or n==1:
#     return n
#   else:
#     return fibo(n-2)+fibo(n-1)

# print(fibo(a))

fibo_list = [0 for _ in range(n+1)]
fibo_list[1] = 1

#주의할 점: range(2,2)인 경우 에러 일어나지 않고 그냥 그대로 끝남
for i in range(2, n+1):
  fibo_list[i] = fibo_list[i-1]+fibo_list[i-2]

print(fibo_list[-1])

