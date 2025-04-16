function solution(k, tangerine) {
    // 1. 귤 크기별 개수 정리
    var tanCounts = new Array(Math.max(...tangerine)+1).fill(0);
    tangerine.forEach(it => tanCounts[it-1]+=1);
    tanCounts = tanCounts.sort((a,b)=> b-a).filter(it => it !== 0);
    
    // 2. 정답 도출
    var gyul = 0; // 귤 개수
    var answer = 0; // 종류 개수
    
    for (let i=0;i<tanCounts.length;i++) {
        gyul += tanCounts[i];
        answer += 1;
        if (gyul >= k) break;
    }
    return answer;
}
