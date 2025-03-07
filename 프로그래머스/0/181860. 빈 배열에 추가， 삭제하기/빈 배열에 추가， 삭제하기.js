function solution(arr, flag) {
    var answer = [];
    arr.forEach((it, i)=> {
        if (flag[i]) {
            for(let i=0;i<(it*2);i++){
                answer.push(it);
            }
        } else {
            for(let i=0;i<(it);i++){
                answer.pop();
            }
        }
    })
    return answer;
}