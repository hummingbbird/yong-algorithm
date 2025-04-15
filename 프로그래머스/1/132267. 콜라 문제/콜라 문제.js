function solution(a, b, n) {
    var answer = 0;
    var coke = n;
    while (coke >= a) {
        answer += Math.floor(coke/a)*b;
        coke = Math.floor(coke/a)*b + (coke%a);
    }
    return answer;
}