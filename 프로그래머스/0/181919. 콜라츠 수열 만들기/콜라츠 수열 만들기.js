function solution(n) {
    var answer = [];
    var num = n;
    while (num > 1) {
        answer.push(num);
        num = num%2==0? (num/2):((3*num)+1);
    }
    answer.push(1);
    return answer;
}
