function cal(n, m) {
    var M = '';
    M += m;
    return (n*(10**M.length)) + m;
}

function solution(a, b) {
    return cal(a, b) > 2*a*b ? cal(a, b) : 2*a*b;
}