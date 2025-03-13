function solution(arr, n) {
    return arr.map((it, i)=> {
        if (arr.length % 2 !== 0) {
            return i%2 === 0? it+n: it;
        } else {
            return i%2 !== 0? it+n: it;
        }
    })
}