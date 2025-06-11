def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = [0] * bridge_length
    
    while 0 < len(truck_weights):
        bridge.pop(0)
        if sum(bridge) + truck_weights[0] > weight:
            bridge.append(0)
        else: 
            bridge.append(truck_weights.pop(0))
        cnt+=1
    return cnt+bridge_length
