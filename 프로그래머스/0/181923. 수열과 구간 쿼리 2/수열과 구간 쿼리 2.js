function solution(arr, queries) {
    var answer = [];
    queries.forEach(([s, e, k])=> {
        var tmp = arr.slice(s, e+1);
        tmp = tmp.filter(number => number > k);
        tmp.sort(function (a, b) {
            return a-b;
        });
        answer.push(tmp.length==0? -1:tmp[0]);
    })
    return answer;
}