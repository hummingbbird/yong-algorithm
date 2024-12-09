nums = list(input().split("-"))
# print(nums)
# -를 최대한 마지막에 할수록 연산의 결과가 작아짐
# ['55', '50+40']
afterCal=[] # 저 리스트를 반복해서 각각의 덧셈 결과를 저장함
for num in nums:
  tmp=num.split("+")
  numsum=0
  for t in tmp:
    numsum+=int(t)
  afterCal.append(numsum)

n = afterCal[0]

for i in range(1, len(afterCal)):
  n-=afterCal[i]
print(n)