function solution(arr, query) {
    var answer = arr;
    query.forEach((_, idx)=> {
        if (idx%2==0) {
            answer = answer.slice(0, query[idx]+1);
        } else {
            answer = answer.slice(query[idx], answer.length);
        }
        console.log("answer: ", answer);
    })
    return answer;
}