function solution(a, d, included) {
    var answer = 0;
    const n = included.length;
    var cntA = 0;
    var cntD = 0;
    for (let i=0; i<n;i++){
        if (included[i] === true) {
            cntA += 1;
            cntD += i;
        }
    }
    return (a*cntA)+(d*cntD);
}