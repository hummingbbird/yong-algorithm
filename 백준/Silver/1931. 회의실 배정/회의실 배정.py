# https://www.acmicpc.net/problem/1931

N = int(input())
Is = [list(map(int, input().split(" "))) for _ in range(N)]

# 1. 종료시간 기준 정렬
Is.sort(key=lambda x:[x[1], x[0]])

cnt=0
for i in range(N):
  if i==0:
    finish_time = Is[i][1]
    cnt+=1
  # 시작 시간=종료 시간인 경우 cnt++
  elif Is[i][0] == Is[i][1]:
    finish_time = Is[i][1]
    cnt+=1
  else:
    if Is[i][0] < finish_time:
      continue
    else:
      finish_time = Is[i][1]
      cnt+=1
print(cnt)