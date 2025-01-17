function solution(l, r) {
    var answer = [];
    for (let i=l;i<=r;i++){
        let str = String(i);
        if([...str].every(el => el==='5' || el==='0')) {
            answer.push(Number(str));
        }
    }
    return answer.length===0? [-1]:answer;
}