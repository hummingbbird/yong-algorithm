function solution(maps) {
    const n = maps.length, m = maps[0].length;
    
    const bfs = () => {
        const v = [[0,0]]
        
        const visited = [];
        for (let i=0;i<n;i++) {
            visited.push(Array(m).fill(false));
        }
        visited[0][0] = true;
        
        const distance = Array.from(
            { length: n },
            () => Array(m).fill(0)
        );
        distance[0][0] = 1;
        
        const dx = [-1, 1, 0, 0];
        const dy = [0 ,0, -1, 1];
        
        while (v.length > 0) {
            const [cur_x, cur_y] = v.shift();
            
            for (let i=0;i<4;i++) {
                const nx = cur_x + dx[i];
                const ny = cur_y + dy[i];
                
                if (0<=nx && nx<n && 0<=ny && ny<m && maps[nx][ny] === 1 && visited[nx][ny] === false) {
                    visited[nx][ny] = true;
                    v.push([nx, ny]);
                    distance[nx][ny] = distance[cur_x][cur_y]+1;
                }
            }
        }
        
        if (visited[n-1][m-1] === false) {
            return -1;
        }
        else {
            return distance[n-1][m-1];
        }
    }
    return bfs();
}