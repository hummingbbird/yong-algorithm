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

// 리팩토링 후 코드
function solution2(s, n) {
    var answer = "";
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lower = "abcdefghijklmnopqrstuvwxyz"; // 굳이 toLowerCase 쓰지 말고 한 눈에 들어오게
    for (const it of [...s]) {
        if (it === " ") {
            answer+=" ";
            continue;
        }
        const charArr = upper.includes(it)? upper: lower; // 대소문자 구분을 먼저 진행해서 중복 코드 줄이기
        answer+=charArr[((charArr.indexOf(it)+n)%26)];
    }
    
    return answer;
}
