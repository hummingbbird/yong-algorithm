function solution(array, commands) {
    const answer = [];
    commands.forEach((item) => {
        const [i, j, k] = item;
        answer.push(array.slice(i-1, j).sort((a,b)=>a-b)[k-1]);
    })
    return answer;
}