def solution(name, yearning, photo):
    answer = []
    lonely={}
    #1.점수와 추억점수 매칭
    for i in range(len(name)):
        lonely[name[i]] = yearning[i] 
    
    for photoList in photo:
        a=0
        for p in photoList:
            if p in name:
                a += lonely[p]
            else:
                continue
        answer.append(a)
            
    
        
    return answer