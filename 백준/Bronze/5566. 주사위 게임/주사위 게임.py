#1. 초기 세팅(입력값 받아서 정리)
a, b = map(int, input().split())

board = []
for _ in range(a):
  board.append(int(input()))

marble = []
for _ in range(b):
  marble.append(int(input()))

#2. 반복문을 돌려 주사위를 이동 시켜요(while문을 써봐요)
#최대 반복 회수는 b, 그보다 작을 때는 조건문으로 확인하여 break해주어요
#total=0으로 시작, 10을 넘을 시 종료
#idx=0 현재 커서의 index정도로 생각
#current: 입력받은 주사위 눈
cnt = 1
idx = 0
result = 0
for i in range(b):
  if marble[i]+idx > len(board)-2:
    result = marble[i]+idx
    print(i+1)
    break
  idx += marble[i] + board[marble[i]+idx]
  if idx > len(board)-2:
    print(i+1)
    break


