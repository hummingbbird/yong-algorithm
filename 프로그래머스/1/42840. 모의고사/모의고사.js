function solution(answers) {
    var score = [0,0,0];
    const p1 = [1,2,3,4,5];
    const p2 = [2,1,2,3,2,4,2,5];
    const p3 = [3,3,1,1,2,2,4,4,5,5];
    for (let i=0;i<answers.length;i++) {
        if (p1[i%5] === answers[i]) {score[0]++;}
        if (p2[i%8] === answers[i]) {score[1]++;}
        if (p3[i%10] === answers[i]) {score[2]++;}
    }
    const ans = [];
    score.forEach((item, idx) => {if (item === Math.max(...score)) ans.push(idx+1)});
    return ans;
}