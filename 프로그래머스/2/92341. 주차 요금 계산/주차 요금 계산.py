import math

def changeToMinute(s, e):
    s_hh, s_mm = s.split(":")
    e_hh, e_mm = e.split(":")
    return ((int(e_hh) * 60) + int(e_mm)) - ((int(s_hh) * 60) + int(s_mm))

def calculator(fees, time):
    [std, std_fee, unit, unit_fee] = fees
    if time <= std:
        return std_fee
    else:
        return std_fee + (math.ceil((time-std)/unit) * unit_fee)
        
    
def solution(fees, records):
    dic = {}
    for item in records:
        time, num, r = item.split(" ")
        if num in dic.keys():
            dic[num].append(time)
        else:
            dic[num] = [time]
    
    for k in dic.keys():
        if len(dic[k]) % 2 == 1:
            dic[k].append("23:59")
    
    total_dic = {}
    
    for k in dic.keys():
        total = 0
        for i in range(0, len(dic[k]), 2):
                total += changeToMinute(dic[k][i], dic[k][i+1])
        total_dic[k] = total
    total_dic = sorted(total_dic.items())
    
    ans = []
    for item in total_dic:
        ans.append(calculator(fees, item[1]))
        
    return ans