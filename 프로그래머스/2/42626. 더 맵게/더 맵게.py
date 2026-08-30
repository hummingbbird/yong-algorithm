import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
        answer += 1
    
    if len(scoville) < 2 and scoville[0] < K:
        answer = -1
        
    return answer

