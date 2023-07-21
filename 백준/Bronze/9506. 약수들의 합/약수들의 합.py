while True:
    n = int(input())
    yaksu=[]
    if n == -1:
        break
    for i in range(1, n):
        if n%i == 0:
            yaksu.append(i)
    if sum(yaksu) == n:
        a = str(n) + " = "
        a = a + " + ".join(map(str, yaksu))
        print(a)
    else:
        print("{0} is NOT perfect.".format(n))
