n = int(input())
print((2**n)-1)

def hanoi(start, end, middle, n):
    if n == 1:
        print(f"{start} {end}")
    else:
        hanoi(start, middle, end, n-1)
        print(f"{start} {end}")
        hanoi(middle, end, start, n-1)

hanoi(1, 3, 2, n)