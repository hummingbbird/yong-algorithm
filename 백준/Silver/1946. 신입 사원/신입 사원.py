import sys
# https://www.acmicpc.net/problem/1946

T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  freshmen = []
  for _ in range(N):
    # 이 때 입력되는 건 순위임(점수 아님)
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    freshmen.append(tmp)

  # 1. 일단 정렬해서 1번 항목의 순위는 순서를 보장하고 진행
  freshmen = sorted(freshmen)

  #2. 
  answer=1
  topRank = 100001
  for i in range(N):
    if i==0:
      topRank=freshmen[i][1]
      continue
    else:
      if freshmen[i][1] < topRank: # 내 순위가 더 높으면
        topRank = freshmen[i][1]
        answer+=1
      
      
  print(answer)