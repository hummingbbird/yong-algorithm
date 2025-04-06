function solution(arr) {
    const w = arr[0].length > arr.length? arr[0].length: arr.length;
    var answer = [];
    
    for(let i=0;i<w;i++) {
        let tmp = new Array(w).fill(0);
        if (arr[0].length <= w && i<arr.length) {
            for(let j=0;j<arr[0].length;j++) {
                tmp[j] = arr[i][j];
            }
        }
        answer.push(tmp);
    }
    return answer;
}