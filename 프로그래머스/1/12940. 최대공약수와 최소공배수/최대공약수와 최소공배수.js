// 1. 기본
const GCD = (a, b) => {
    // 1부터 min(a, b)까지 a, b를 나눠서 0이 되는 수로 update
    let g = 1;
    for(let i=0;i<=Math.min(a, b);i++) {
        if (a%i === 0 && b%i === 0) g = i;
    }
    return g;
}

const LCM = (a, b) => {
    // 1부터 무한반복 -> l을 a, b로 나눈 나머지가 모두 0이면 break
    var l = 1;
    while (true) {
        if(l%a === 0 && l%b === 0) return l;
        l++;
    }
}

// 2. 유클리드 호제법을 사용한 풀이
const EuclideanGCD = (a, b) => a%b === 0? b: EuclideanGCD(b, a%b);
const EuclideanLCM = (a, b) => (a*b)/EuclideanGCD(a, b);

function solution(n, m) {
    return [EuclideanGCD(n, m), EuclideanLCM(n, m)];
}