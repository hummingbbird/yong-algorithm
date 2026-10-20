function solution(participant, completion) {
    let answer = '';
    // 1. 해시로 정리
    const dic = {};
    participant.forEach((item) => {
        if (dic[item]) {
            dic[item] += 1
        }
        else {
            dic[item] = 1
        }
    })
    
    // 2. completion 탐색
    completion.forEach((item) => {
        dic[item] -= 1
    })
    return Object.keys(dic).filter((item) => dic[item] === 1).join('');
}