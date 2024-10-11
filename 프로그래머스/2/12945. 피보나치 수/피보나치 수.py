
def solution(n):
    numbers = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if i==1:
            numbers[i]=1
        else:
            numbers[i] = numbers[i-1]+numbers[i-2]
    return numbers[-1]%1234567