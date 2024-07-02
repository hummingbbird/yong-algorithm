a = int(input())
if a == 1:
  print(1)
elif a == 2:
  print(3)
else:
  result = [1,3]
  for i in range(2, a):
    result.append(result[i-2]*2+result[i-1])
  print(result[-1]%10007)