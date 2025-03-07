function solution(arr) {
    var answer = [];
    arr.forEach(it=> {
        for (let i=0;i<it;i++) {
        answer.push(it);
        }
    })
    return answer;
}