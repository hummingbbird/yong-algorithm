function solution(my_string, k) {
    var answer = '';
    // 1. 일반 반복문
    // for (let i=0; i<k;i++) {
    //     answer += my_string;
    // }
    
    // 2. repeat 내장함수
    answer = my_string.repeat(k);
    return answer;
}