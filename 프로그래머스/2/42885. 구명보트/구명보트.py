def solution(people, limit):
    i, j = 0, len(people)-1
    people.sort(reverse=True)
    
    while True:
        if people[i]+people[j] <= limit:
            j-=1
        i+=1
        if i>j:
            break
        elif i==j:
            i+=1
            break
    return i