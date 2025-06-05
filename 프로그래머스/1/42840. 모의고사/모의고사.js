function solution(answers) {
    var answer = [0,0,0];
    const first = "12345";
    const second = "21232425";
    const third = "3311224455";
    answers.forEach((it, i) => {
        if (it.toString() === first[i%5]) answer[0]++;
        if (it.toString() === second[i%8]) answer[1]++;
        if (it.toString() === third[i%10]) answer[2]++;
    });
    return answer.map((it, i) => {
        if (it === Math.max(...answer)) return i+1;
    }).filter(it => it);
}