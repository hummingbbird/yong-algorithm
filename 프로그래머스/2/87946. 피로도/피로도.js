function solution(k, dungeons) {
    let maxCount = 0;
    
    const visited= Array(dungeons.length).fill(false);
    
    const dfs = (cur_k, cnt) => { 
        for (let i=0;i<dungeons.length;i++) {
            if (cur_k >= dungeons[i][0] && visited[i] === false) {
                visited[i] = true;
                dfs(cur_k - dungeons[i][1], cnt+1);
                visited[i] = false;
            }
        }
        
        maxCount = Math.max(cnt, maxCount);
    }
    
    dfs(k, 0);
    return maxCount;
}