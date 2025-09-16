# 재귀 알고리즘의 대표 문제
# hanoi 인자값: 시작, 끝, 중간, answer 리스트, 개수

def hanoi(start, end, middle, answer, n):
    if n == 1:
        answer.append([start, end])
    else:
        # 1. n-1개를 2번 막대로 옮기는 작업
        hanoi(start, middle, end, answer, n-1)
        
        # 2. 바닥을 3번 막대로 옮김
        answer.append([start, end])
        
        # 3. 2번 막대에 있는 n-1개를 3번 막대로 옮기는 작업
        hanoi(middle, end, start, answer, n-1)
    

def solution(n):
    answer = []
    hanoi(1, 3, 2, answer, n)
    return answer
