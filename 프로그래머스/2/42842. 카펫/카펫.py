def solution(brown, yellow):
    entire = brown+yellow
    answer=[]
    # 곱해서 yellow가 되는 두 수를 구하고 걔네에 2씩 더해서 곱한 거랑 brown+yellow랑 같으면 정답
    # 1. 약수 찾기를 진행해야하나?
    num=1
    while num <(entire/2)+1:
        if entire % num == 0:
            a, b = num, entire//num
            print(a, b)
            if (a-2)*(b-2) == yellow:
                return [b, a]
                break
            else:
                num+=1
                continue
        else:
            num+=1
    return answer