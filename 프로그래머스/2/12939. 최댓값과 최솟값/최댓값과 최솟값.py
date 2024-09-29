def solution(s):
    numbers = list(int(i) for i in s.split(" "))
    answer = str(sorted(numbers)[0])+" "+str(sorted(numbers)[-1])
    return answer