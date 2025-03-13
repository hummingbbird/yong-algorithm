function solution(arr, n) {
    return arr.map((it, i)=> {
        if (arr.length % 2 !== 0) {
            return i%2 === 0? it+n: it;
        } else {
            return i%2 !== 0? it+n: it;
        }
    })
}

const solution2 = (arr, n) => arr.map((it, i)=> (
        arr.length%2 !== i%2? it+n:it
    ))

function solution3 (arr, n) {
    return arr.map((it, i)=> {
        if (arr.length % 2 !== 0) {
            return i%2 === 0? it+n: it;
        } else {
            return i%2 !== 0? it+n: it;
        }
    })
}
