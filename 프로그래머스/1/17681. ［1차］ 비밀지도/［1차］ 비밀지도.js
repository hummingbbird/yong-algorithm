const getBinary = (n, tgt) => {
    const changed = tgt.toString(2);
    return ("0".repeat(n-changed.length)+changed);
}

function solution(n, arr1, arr2) {
    var answer = [];
    // 1. arr1, arr2 2진수 변환
    arr1 = arr1.map(it => getBinary(n, it));
    arr2 = arr2.map(it => getBinary(n, it));
    
    // 2. 합집합 구하기
    for(let i=0;i<n;i++) {
        const he = new Array(n).fill(0).map((_, j)=> (arr1[i][j] === "1" || arr2[i][j]=== "1")? "#":" ").join("");
        answer.push(he);
    }
    return answer;
}