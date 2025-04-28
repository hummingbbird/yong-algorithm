function solution(n, left, right) {
    var answer = [];
    for(let i=Math.floor(left/n);i<=Math.floor(right/n);i++){
        for(let j=0;j<n;j++){
            answer.push((i<j?j:i)+1);
        }
    };
    return answer.slice(left%n, right-left+(left%n)+1);
}