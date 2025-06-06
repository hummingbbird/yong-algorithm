function solution(priorities, location) {
    var answer = 0;
    var prcs = [];
    // 1. [index, priority] 로 구성된 배열 prcs 생성
    priorities.forEach((it, i)=>{
        prcs.push([i, it])
    });
    while (prcs.length >= 0) {
        const tmp = prcs[0];
        prcs = prcs.slice(1, prcs.length);
        if (tmp[1] !== Math.max(...priorities)) {
            prcs.push(tmp);
        }
        else {
            answer++;
            if (tmp[0] === location) {
                return answer;
            }; 
            for(let i=0; i< priorities.length; i++) {
                if (priorities[i] === Math.max(...priorities)) {
                    priorities.splice(i, 1);
                    break;
                }
            };
        };
    };
    
    return answer;
}