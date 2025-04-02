const solution = (arr, k) => {
    return k%2===1? arr.map(it => it*k):arr.map(it => it+k);
};