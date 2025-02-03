function solution(numbers, n) {
    let result = 0;
    // 1. while 문 사용
    // let i = 0;
    // while(result <= n) {
    //     result+=numbers[i];
    //     i++;
    // }
    // return result;
    
    // 2. for 문 사용
    for(let j=0;j<numbers.length;j++) {
        result += numbers[j];
        if (result > n) return result;
    }

}