function solution(elements) {
    var answer = [];
    var circle = elements.concat(elements);
    answer.push(...new Set(elements)); // 길이가 1인 연속 부분 수열
    for(let i=2;i<=elements.length;i++) {
        for(let j=0;j<elements.length;j++) {
            answer.push(circle.slice(j, j+i).reduce((accu,it)=>accu+it, 0));
        }
    }
    return [...new Set(answer)].length;
}