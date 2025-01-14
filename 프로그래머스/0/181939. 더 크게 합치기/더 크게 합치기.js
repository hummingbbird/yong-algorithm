function cal(n, m) {
    var M = '';
    M += m;
    return (n*(10**M.length)) + m;
}

function solution(a, b) {
    const sol1 = cal(a, b);
    const sol2 = cal(b, a);
    return sol1>sol2? sol1 : sol2;
}