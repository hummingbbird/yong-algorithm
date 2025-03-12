function solution(arr, k) {
    const setArr = new Set(arr);
    var answer = [...setArr];
    while (answer.length < k) {
            answer.push(-1);
        }
    return answer.length > k? answer.slice(0,k):answer;
}
