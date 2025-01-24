function solution(n, k) {
    var answer = [];
    let i = k;
    for (let i=k;i<=n;i+=k) {
        answer.push(i);
    }
    // while (i <= n) {
    //     answer.push(i);
    //     i += k;
    // }
    return answer;
}