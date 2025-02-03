function solution(num_list) {
    // 1. 다양한 array 관련 메소드 사용
    // const odd = num_list.filter((_, i)=> i%2 === 0).reduce((accu, item)=> accu+item);
    // const even = num_list.filter((_, i)=> i%2 !== 0).reduce((accu, item)=> accu+item);
    // return odd>even? odd:even;
    
    let odd = 0;
    let even = 0;
    // 2. 반복문 사용(이게 더 효율적인 것 같다)
    for (let i=0;i<num_list.length;i++) {
        if (i%2===0) odd+=num_list[i];
        else even+=num_list[i];
    }
    return odd>even? odd:even;
}