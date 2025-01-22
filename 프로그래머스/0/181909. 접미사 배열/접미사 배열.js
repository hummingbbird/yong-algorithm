function solution(my_string) {
    var answer = [];
    for(let i=0;i<my_string.length;i++){
        // (0, 6), (1, 6) ... (5,6)
        answer.push(my_string.slice(i, my_string.length));
    }
    return answer.sort();
}