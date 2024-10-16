import sys
# 1. 수 정렬하기
N = int(sys.stdin.readline())
# 0으로 채워진 배열 만들어(counting 용)
cnts = [0 for _ in range(10001)]
# 반복: 해당 index에 +=1 해줍니다.
for _ in range(N):
  num = int(sys.stdin.readline())
  cnts[num]+=1

# index한 대로 출력
for i in range(len(cnts)): 
  if cnts[i] == 0:
    continue
  else:
    for _ in range(cnts[i]):
      print(i)