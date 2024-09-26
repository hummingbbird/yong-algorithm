import re


def solution(s):
    answer = s.lower()
    answer = answer[0].upper() + answer[1:]
    
    # 1. 문자열 s의 공백 index 찾기
    space = " "
    indices = [int(i.start()) for i in re.finditer(space, answer)]
    print(len(s))
    
#     # 2. 각 공백 바로 뒤 문자 대문자로 변경
    for i in indices:
        if i == len(s)-1:
            continue
        answer = answer[:i+1] + answer[i+1].upper() + answer[i+2:]
    
    return answer