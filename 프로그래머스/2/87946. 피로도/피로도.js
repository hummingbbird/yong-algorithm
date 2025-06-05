function solution(k, dungeons) {
    var answer = -1;
    var arr = Array.from({length: dungeons.length}).fill(false);
    function DFS(hp, L) {
        for (let i=0;i<dungeons.length; i++) {
            if (arr[i] === false && hp >= dungeons[i][0]) {
                arr[i] = true;
                DFS(hp-dungeons[i][1], L+1)
                arr[i] = false;
            } 
        }
        
        answer = Math.max(answer, L);
    }
    
    DFS(k, 0)
    return answer;
}