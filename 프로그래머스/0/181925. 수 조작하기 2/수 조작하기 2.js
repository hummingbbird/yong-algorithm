
function solution(numLog) {
    var answer = '';
    // 수의 변화량을 저장하는 리스트 사용하거나 빼가면서 쓰기
    for (let i=1; i<numLog.length;i++){
        const change = numLog[i] - numLog[i-1];
        switch (change) {
            case 1: answer += 'w'; break;
            case -1: answer += 's'; break;
            case 10: answer += 'd'; break;
            case -10: answer += 'a'; break;
        }
    }
    return answer;
}