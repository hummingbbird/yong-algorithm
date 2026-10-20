function solution(progresses, speeds) {
    let answer = [];
    
    while (progresses.length !== 0) {
        // 진행도 업데이트
        progresses = progresses.map((ele, idx) => {
            return ele+speeds[idx]
        })
        // 조건: 맨 앞 원소 100 달성 시 반복
        if (progresses[0] >= 100) {
            let cnt = 0;
            while (progresses[0] >= 100) {
                cnt++;
                progresses.shift()
                speeds.shift()
            }
            if (cnt !== 0) answer.push(cnt);
        }
        
    }
    return answer;
}