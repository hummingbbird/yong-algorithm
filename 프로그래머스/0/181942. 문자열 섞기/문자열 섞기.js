function solution(str1, str2) {
    var answer = '';
    // 이중 포문..이 아니라.. 아 둘이 길이가 같군아.
    const lengthOfStr = str1.length;
    [...str1].forEach((it, idx)=> {
        answer += str1[idx]
        answer += str2[idx]
    })
    return answer;
}