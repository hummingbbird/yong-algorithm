function solution(my_string, queries) {
    var answer = my_string;
    queries.map(([s,e]) => {
        const front = answer.substring(0, s);
        const middle = [...answer.substring(s, e+1)].reverse().join('');
        const back = answer.substring(e+1, my_string.length);
        answer = front + middle + back;
    })
    return answer
}