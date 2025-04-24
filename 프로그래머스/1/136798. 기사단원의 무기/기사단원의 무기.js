// 기본적인데.. 무조건 시간초과남!!!
const getYaksuCount = (n)=> {
    let cnt = 0;
    for(let i=1;i<=Math.sqrt(n);i++) {
        // 16/4=4처럼 제곱이면 +1, 그렇지 않은 경우 대칭이므로 +2
        if (n%i===0) cnt += n/i===i? 1:2;
    };
    return cnt;
};

function solution(number, limit, power) {
    var answer = 0;
    var yaksu = [];
    for(let i=1;i<=number;i++) {
        yaksu.push(getYaksuCount(i)>limit?power:getYaksuCount(i));
    };
    return yaksu.reduce((accu,item) => accu+item,0);
}