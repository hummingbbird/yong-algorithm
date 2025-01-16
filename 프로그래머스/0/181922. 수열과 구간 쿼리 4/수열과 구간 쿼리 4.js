function solution(arr, queries) {
    var answer = arr;
    queries.forEach(([s, e, k])=> {
        arr.map((it, idx)=> {
            if (s <= idx && idx <= e && idx%k==0){
                answer[idx] += 1;
            }
        })
        
    })
    return answer;
}