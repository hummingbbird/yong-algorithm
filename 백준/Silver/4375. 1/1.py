while True:
    try:
        n = int(input())
    except:
        break
    a=1
    digit=1
    while a%n != 0:
        a += 10**digit
        digit += 1
    print(digit)