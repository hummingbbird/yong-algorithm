function solution(arr) {
    return arr.map((it) => {
        if (it >= 50 && it%2===0) {
            return it/2;
        } else if (it < 50 && it%2!==0) {
            return it*2;
        } else return it;
    });
}