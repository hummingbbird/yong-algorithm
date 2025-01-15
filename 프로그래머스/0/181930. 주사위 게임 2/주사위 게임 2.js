function solution(a, b, c) {
    var cnt = 0;
    if (a===b) cnt+=1;
    if (b===c) cnt+=1;
    if (c===a) cnt+=1;
    // 1. 세 숫자가 다 다르면 a+b+c
    if (cnt===0) {
        return a+b+c;
    } else if (cnt===1){
        return (a + b + c) * (a**2 + b**2 + c**2);
    } else {
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3);
    }
}