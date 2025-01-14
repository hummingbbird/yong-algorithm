function solution(ineq, eq, n, m) {
    var answer = false;
    const sign = ineq+eq;
    console.log("sign: "+sign);
    switch (sign) {
        case "<=":
            answer = (n <= m);
            break;
        case ">=":
            answer = (n >= m);
            break;
        case ">!":
            answer = (n > m);
            break;
        case "<!":
            answer = (n < m);    
            break;
    }
    return answer? 1:0;
}