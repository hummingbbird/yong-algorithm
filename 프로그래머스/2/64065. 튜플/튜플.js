function solution(s) {
    var answer = [];
    // 1. s를 리스트 형태로 변환
    var tuple = s.slice(2, s.length-2).split("},{").map(it=> {
        return it.split(",").map(it => parseInt(it));
    });
    
    // 2. 배열 길이 기준 오름차순 정렬
    tuple.sort(function(a,b){
        return a.length-b.length;
    });
    
    // 3. 완성하기
    tuple.forEach((it, i)=> {
        answer.push(it.filter(ele => !answer.includes(ele))[0]);
    })
    
    return answer;
}

// 리팩토링한 코드 .. 지만? 난 기존 게 더 가독성이 좋다고 생각 .. ~~
function solution2(s) {
    var answer = [];
    
    var tuple = s.slice(2, s.length-2).split("},{")
    .map(it=> it.split(",").map(it => parseInt(it)))
    .sort(function(a,b){return a.length-b.length;})
    .forEach((it, i)=> {
        answer.push(it.filter(ele => !answer.includes(ele))[0]);
    });
    
    return answer;
}
