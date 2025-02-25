function solution(binomial) {
    const [a, op, b] = binomial.split(" "); // 구조 분해 할당
    switch (op) {
        case "+":
            return +a + +b; // 문자열 덧셈이 되지 않기 위한 처리 필요
        case "-":
            return a-b;
        case "*":
            return a*b;
    }
}
