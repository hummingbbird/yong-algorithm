function solution(num_list) {
    var answer = num_list.sort(function(a, b) {
        return a-b;
    })
    return answer.slice(5, answer.length);
}