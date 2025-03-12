function solution(arr) {
    let i = 0;
    while (2**i < arr.length) {
        i++;
    }
    return [...arr, ...Array((2**i)-arr.length).fill(0)];
}