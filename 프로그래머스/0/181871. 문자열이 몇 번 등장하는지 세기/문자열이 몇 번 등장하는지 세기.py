def solution(myString, pat):
    answer = 0
    n = len(pat)
    for i in range(0, len(myString)-n+1):
        if myString[i:i+n] == pat:
            answer += 1
    return answer