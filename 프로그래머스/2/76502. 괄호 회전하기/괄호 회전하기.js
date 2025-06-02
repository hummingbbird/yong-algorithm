function isRight(str) {
    let stack = [];
    for (const s of [...str]) {
        if (stack.length===0) {
            stack.push(s);
            continue;
        }
        else if ("({[".includes(s)) {
            stack.push(s);
        }
        else if (s === ")") {
            if (stack[stack.length-1] === "(") {
                stack.pop();
            } else {
                stack.push(s);
            }
        }
        else if (s === "}") {
            if (stack[stack.length-1] === "{") {
                stack.pop();
            } else {
                stack.push(s);
            }
        }
        else if (s === "]") {
            if (stack[stack.length-1] === "[") {
                stack.pop();
            } else {
                stack.push(s);
            }
        };
        // console.log("stack:", stack);
    }
    return stack.length===0?true:false;
};

function solution(s) {
    var answer = 0;
    for(let i=0;i<s.length;i++) {
        if (isRight(s.slice(i,s.length)+s.slice(0,i))) {
            answer++;
        };
    }
    // isRight("{(})");
    return answer;
}