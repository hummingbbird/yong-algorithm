function solution(picture, k) {
    var answer = [];
    picture.forEach((it)=> {
        for(let i=0;i<k;i++) {
            answer.push([...it].map(it => it.repeat(k)).join(""));
        }        
    })
    return answer;
}