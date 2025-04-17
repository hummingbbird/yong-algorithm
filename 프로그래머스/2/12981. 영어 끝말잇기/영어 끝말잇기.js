// 1. 번호는 (i%n)+1, 차례는 Math.floor(i/n)+1 과 같습니다.
function solution(n, words) {
    var answer = [];
    for (let i=1;i<words.length;i++) {
        const player = (i%n)+1;
        const time = Math.floor(i/n)+1;
        const wordLength = words[i-1].length;
        if (words[i-1][wordLength-1] !== (words[i][0])
           || words.slice(0, i).includes(words[i])
           ) {
            return [player, time];
        }
    }

    return [0,0];
}