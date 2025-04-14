function solution(s) {
    var answer = [];
    var maxIndex = {};
    
    [...s].forEach((it, i)=> {
        Object.keys(maxIndex).includes(it)?
            answer.push(i-maxIndex[it]):answer.push(-1);
        maxIndex[it] = i;
    })
    return answer;
}