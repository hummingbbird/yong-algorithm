function solution(my_string, index_list) {
    var answer = '';
    index_list.map((it)=> {
        answer += my_string[it];
    })
    return answer;
}