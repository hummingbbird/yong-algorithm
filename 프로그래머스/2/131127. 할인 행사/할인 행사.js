function solution(want, number, discount) {
    var answer = 0;
    // 1. wants 배열 만들기
    var wants = [];
    want.map((it, i) => {
        for(let j=0;j<number[i];j++) {
            wants.push(it);
        }
    });
    
    // 2. discount 돌기
    for(let i=0;i<discount.length-10+1;i++){
        const discountRange = discount.slice(i, i+10);
        // 배열에서 개수 세서 더한 값이 10이 되면.. 다음은 어떡하지?
        const tmp = want.reduce((accu, item, i)=> {
            if(discountRange.filter(it=>it === item).length === number[i]){
                return accu+number[i];
            }
        },0);
        answer += tmp===10? 1:0;
        };
    return answer;
}