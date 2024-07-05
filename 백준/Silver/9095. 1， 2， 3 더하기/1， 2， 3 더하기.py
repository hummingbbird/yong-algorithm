a = int(input())
# ans = [0,1,2,4,7,13,24,44,81,149,274]

for _ in range(a):
  n = int(input())
  if n == 1 or n == 2:
    print(n)
    continue
  #3부터 여기를 온다는 뜻
  cases = [0 for i in range(n+1)]
  cases[0] = 1
  cases[1] = 1
  cases[2] = 2
  for i in range(3, n+1):
    cases[i] = cases[i-1] + cases[i-2] + cases[i-3]
  print(cases[n])