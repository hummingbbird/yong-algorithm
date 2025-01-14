function solution(n) {
    var answer = 0;
    // 7 -> 1 3 5 7
    // 10 -> 2 4 6 8 10의 제곱의 합
    if (n%2==0) {
        for (let i=2;i<=n;i+=2){
            answer += i**2
        }
    } else {
        for (let i=1;i<=n;i+=2){
            answer += i
        }
    }
    return answer;
}