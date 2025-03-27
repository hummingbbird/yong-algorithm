function solution(strArr) {
    var lst = [];
    // 1. 그룹으로 묶기
    strArr.forEach(it => {
        lst.push(it.length);
    })
    // 2. 개수 중에 큰 거 return
    var answer = 0;
    for(let i=1;i<31;i++) {
        const tmp = lst.filter(it => it === i).length;
        answer = tmp>=answer? tmp:answer;
    }
    
    return answer;
}