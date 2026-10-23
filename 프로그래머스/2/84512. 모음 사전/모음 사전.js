function solution(word) {
    var answer = 0;
    const moem = ["A","E","I", "O", "U"];
    const entire = [];
    const bfs = (cur,idx) => {
        if (idx > 5) {
            return;
        }
        for (let i=0;i<5;i++) {
            entire.push(cur + moem[i]);
            bfs(cur+moem[i], idx+1)
        }
    };
    bfs("", 1)
    return entire.indexOf(word) + 1;
}