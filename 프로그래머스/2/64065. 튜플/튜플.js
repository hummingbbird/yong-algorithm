function solution(s) {
    var answer = [];
    // 1. s를 리스트 형태로 변환
    var ss = s.slice(2, s.length-2).split("},{").map(it=> {
        return it.split(",").map(it => parseInt(it));
    });
    
    // 2. 배열 길이 기준 오름차순 정렬
    ss.sort(function(a,b){
        return a.length-b.length;
    });
    
    // 3. 완성하기
    ss.forEach((it, i)=> {
        answer.push(it.filter(ele => !answer.includes(ele))[0]);
    })
    
    return answer;
}