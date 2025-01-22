function solution(intStrs, k, s, l) {
    var answer = [];
    for (let i=0;i<intStrs.length;i++){
        const sliced = intStrs[i].substr(s, l);
        // answer.push(Number(sliced))
        if (k < Number(sliced)) {
            answer.push(Number(sliced));
        }
    }
    return answer;
}