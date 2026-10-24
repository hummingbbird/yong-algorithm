function solution(n, wires) {
    let minDifference = Infinity; 

    // 1. 간선을 하나씩 차례대로 없애보는 전체 순회 (완전탐색)
    for (let i = 0; i < wires.length; i++) {
        // i번째 간선을 제외한 나머지 간선들로 그래프 구성
        const graph = Array.from({ length: n + 1 }, () => []);
        
        for (let j = 0; j < wires.length; j++) {
            if (i === j) continue; // 끊어낼 간선 스킵
            const [v1, v2] = wires[j];
            graph[v1].push(v2);
            graph[v2].push(v1);
        }

        const count = bfs(1, graph, n);

        const otherCount = n - count;
        const diff = Math.abs(count - otherCount);
        minDifference = Math.min(minDifference, diff);
    }
    return minDifference;
}

function bfs(startNode, graph, n) {
    const visited = Array(n + 1).fill(false);
    const queue = [startNode];
    visited[startNode] = true;
    
    let count = 0;

    while (queue.length > 0) {
        const currentNode = queue.shift();
        count++;

        for (const nextNode of graph[currentNode]) {
            if (!visited[nextNode]) {
                visited[nextNode] = true;
                queue.push(nextNode);
            }
        }
    }

    return count;
}