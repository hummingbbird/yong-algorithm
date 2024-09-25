def solution(s):
    # (가 있고 )가 들어온 경우 둘 다 없애 애니팡 게임처럼
    # ( 없는데 ) 들어오면 바로 false 하고 끝내
    # 이런식이면 될랑가?
    leftNum = 0
    for gwalho in s:
        if gwalho == ")": # 오른쪽 괄호가 들어왔을 때
            if leftNum > 0: # 왼 괄호가 있으면
                leftNum -= 1 # 애니팡 펑
            else: # 왼 괄호가 없으면 -> 틀린 거니까 리턴
                return False
        else:
            leftNum += 1
    if leftNum == 0:
        return True
    else:
        return False
