function solution(arr, intervals) {
    var answer = [];
    intervals.map((interval)=> {
        answer=answer.concat([...arr.slice(interval[0],interval[1]+1)]);
    })
    return answer;
    
    // 다른 사람의 풀이(better)
    const [[a,b],[c,d]] = intervals; // 일케하면 각 원소가 a,b,c,d에 저장됨
    return [...arr.slice(a,b+1), ...arr.slice(c, d+1)]; // spread 연산자 활용
}
