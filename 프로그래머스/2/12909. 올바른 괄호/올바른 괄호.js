function solution(s){
    const stack = [];
    [...s].forEach((item) => {
        if (stack.length === 0) {
            stack.push(item);
        }
        else if (item===")" && stack.at(-1) === "(") {
            stack.pop();
        }
        else {
            stack.push(item);
        }
    })
    return stack.length === 0;
}