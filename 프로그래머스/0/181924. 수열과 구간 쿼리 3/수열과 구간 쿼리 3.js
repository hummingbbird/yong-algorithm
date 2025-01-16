function solution(arr, queries) {
    var answer = arr;
    queries.map((item)=> {
        const tmp = answer[item[1]];
        answer[item[1]] = answer[item[0]];
        answer[item[0]] = tmp;
    })
    return answer;
}