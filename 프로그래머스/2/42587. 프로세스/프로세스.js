function solution(priorities, location) {
    // location은 인덱스로 접근, 정답은 일반 숫자로 접근(1번째 2번째 ..)
    // 지금 pop된 애의 [0]이 location이랑 같으면 order return~
    let order = 1;
    const queue = [];
    
    for(let i=0;i<priorities.length;i++) {
        queue.push([i, priorities[i]]);
    }
    
    while (true) {
        const now = queue.shift();
        if (Math.max(...queue.map((item) => item[1])) <= now[1]){
            if (now[0] === location){
                return order;
            }
            else {
                order++;
            };
        }
        else {
            queue.push(now);
        }
    }
}