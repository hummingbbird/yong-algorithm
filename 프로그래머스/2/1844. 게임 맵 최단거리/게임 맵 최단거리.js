function solution(maps) {
    const N = maps.length;
    const M = maps[0].length;
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    
    let tovisit = [];
    tovisit.push([0,0]);
    
    while (tovisit.length !== 0) {
        const [cx, cy] = tovisit.shift();
        for(let i=0;i<4;i++) {
            const nx = cx + dx[i];
            const ny = cy + dy[i];
            
            if (0 <= nx && nx < N && 0 <= ny && ny < M && maps[nx][ny] == 1) {
                tovisit.push([nx, ny]);
                maps[nx][ny] = maps[cx][cy] + 1;
            }
        }
    }
    
    return maps[N-1][M-1] === 1? -1: maps[N-1][M-1];
}