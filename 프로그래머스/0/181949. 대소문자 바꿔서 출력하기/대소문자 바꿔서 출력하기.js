const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let answer = "";
    // 대문자는 소문자로, 소문자는 대문자로
    [...str].forEach((e, i) => {
        if (e === e.toUpperCase()) {
            answer=answer+e.toLowerCase();
        } else {
            answer=answer+e.toUpperCase();
        }
    })
    console.log(answer);
});