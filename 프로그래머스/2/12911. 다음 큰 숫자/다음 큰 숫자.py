def solution(n):
    # 1. n보다 큰 자연수일 것
    # 2. 2진수로 변환했을 때 1의 개수가 같음
    numOf1 = str(bin(n)).count("1")
    answer = n
    while True:
        answer+=1
        if str(bin(answer)).count("1") == numOf1:
            break
    return answer