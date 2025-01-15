function solution(num_list) {
    const multiply = num_list.reduce((accum, item)=> accum*item);
    const hap = num_list.reduce((accum, item)=> accum+item, 0);
    const sqrt = hap*hap;
    console.log("곱: ", multiply, "합의제곱: ", sqrt);
    return multiply < sqrt? 1:0;
}