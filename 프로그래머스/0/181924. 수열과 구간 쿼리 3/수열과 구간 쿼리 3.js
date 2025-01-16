function solution(arr, queries) {
    var answer = arr;
    queries.map((item)=> {
        const tmp = answer[item[1]];
        answer[item[1]] = answer[item[0]];
        answer[item[0]] = tmp;
    })
    return answer;
}

// 구조 분해 할당으로 푸는 방법. 어케 생각함????? ㅠㅠ
function solution(arr, queries) {
    queries.forEach( ([a,b]) => {
        [arr[a],arr[b]] = [arr[b],arr[a]];
    })
    return arr;
}
