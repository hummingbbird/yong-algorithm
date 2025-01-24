function solution(my_string, indices) {
    var answer = '';
    [...my_string].map((it, i)=> {
        if (!(indices.includes(i))) {
            answer += it;
        } 
    })
    return answer;
}