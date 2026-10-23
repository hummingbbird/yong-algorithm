const whichHand = (now, l, r, hand) => {
    // 왼/오 각각 손과 키패드의 거리 계산
    const dist_l = Math.abs(now[0]-l[0]) + Math.abs(now[1]-l[1]);
    const dist_r = Math.abs(now[0]-r[0]) + Math.abs(now[1]-r[1]);
    if (dist_l < dist_r) {
        return ["L", 0];
    } else if (dist_l > dist_r) {
        return ["R", 1];
    }
    return [hand==="left"? "L":"R", hand==="left"?0:1];
}

function solution(numbers, hand) {
    const keypad = [[3,1],
                    [0,0],[0,1],[0,2],
                    [1,0],[1,1],[1,2],
                    [2,0],[2,1],[2,2]];
    var answer = '';
    let cur = [[3,0], [3,2]]
    
    numbers.forEach((i) => {
        if (i % 3 === 1) { // 1 4 7 
            answer += "L";
            cur[0] = keypad[i];
        }
        else if (i !== 0 && i % 3 === 0) { // 3 6 9
            answer += "R";
            cur[1] = keypad[i];
        }
        else { // 2 5 8
            const [h, idx] = whichHand(keypad[i], cur[0], cur[1], hand);
            answer += h;
            cur[idx] = keypad[i]; 
        }
    })
    
    return answer;
}