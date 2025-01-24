function solution(my_string, indices) {
    // var answer = '';
    // [...my_string].map((it, i)=> {
    //     if (!(indices.includes(i))) {
    //         answer += it;
    //     } 
    // })
    // return answer;
    return [...my_string].filter((it, i)=>!(indices.includes(i))).join(""); // 한 줄로 리팩토링 ~
}
