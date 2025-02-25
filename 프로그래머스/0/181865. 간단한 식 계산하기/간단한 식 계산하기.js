function solution(binomial) {
    var bino = binomial.split(" ");
    var num1 = Number(bino[0]);
    var num2 = Number(bino[2]);
    switch (bino[1]) {
        case "+":
            return num1+num2;
        case "-":
            return num1-num2;
        case "*":
            return num1*num2;
    }
}