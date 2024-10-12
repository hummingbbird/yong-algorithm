# def changeToBin(x):
#     # x라는 숫자가 들어오면 이걸 이진 변환해
#     while x < 2:
        
#     return num
    
    
    
def solution(s):
    cnt = 0 # 이진 변환 횟수
    numOfZero = 0 # 제거한 0의 개수 
    # print(bin(len(s)))
    while True:
        numOfZero+=s.count("0")
        lenS = (s.count("1"))
        s = str(bin(lenS)[2:])
        print(s)
        cnt+=1
        if len(s) == 1:
            break
        
    return [cnt, numOfZero]