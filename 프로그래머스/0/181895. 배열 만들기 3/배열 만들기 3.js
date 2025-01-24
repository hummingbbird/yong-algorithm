function solution(arr, intervals) {
    var answer = [];
    intervals.map((interval)=> {
        answer=answer.concat([...arr.slice(interval[0],interval[1]+1)]);
    })
    return answer;
}