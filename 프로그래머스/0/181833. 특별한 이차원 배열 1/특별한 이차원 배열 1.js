function solution(n) {
    var answer = [];
    for(let i=0;i<n;i++) {
        let lst = new Array(n).fill(0).map((_, index) => index===i? 1:0);
        answer.push(lst);
    }
    return answer;
}