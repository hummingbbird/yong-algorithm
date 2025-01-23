function solution(my_string) {
    var answer = new Array(52).fill(0);
    // 아스키코드로 변환시 대문자는 65부터, 소문자는 97부터 시작
    // answer에서는 대문자는 0부터, 소문자는 26부터 시작
    [...my_string].map((it)=> {
        answer[it.charCodeAt(0)-(/[a-z]/g.test(it)? 71:65)] += 1;
        // if (/[a-z]/g.test(it)) {
        //     answer[it.charCodeAt(0)-71] += 1;
        // } else {
        //     answer[it.charCodeAt(0)-65] += 1;
        // }
        
    })
    
    return answer;
}