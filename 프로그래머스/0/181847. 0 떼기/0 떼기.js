function solution(n_str) {
    for (var i=0; i<10;i++) {
        if (n_str[i] !== "0") break;
    }
    return n_str.slice(i, n_str.length);
}