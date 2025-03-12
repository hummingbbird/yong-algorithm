function solution(arr, k) {
    const setArr = new Set(arr);
    var answer = [...setArr];
    if (answer.length > k){
        answer=answer.slice(0, k);
    } else {
        while (answer.length < k) {
            answer.push(-1);
        }
    }
    return answer;
}