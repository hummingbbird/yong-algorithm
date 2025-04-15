function solution(s, n) {
    var answer = "";
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lower = upper.toLowerCase();
    for (const it of [...s]) {
        if (it === " ") {
            answer+=it;
            continue;
        }
        if (it.search(/[a-z]/g)!==-1) answer+=lower[((lower.indexOf(it)+n)%26)];
        else answer+=upper[((upper.indexOf(it)+n)%26)];
    }
    
    return answer;
}