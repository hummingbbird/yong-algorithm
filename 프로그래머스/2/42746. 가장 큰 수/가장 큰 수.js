function solution(numbers) {
    // 모두 0인 경우 "0" 리턴
    if (numbers.reduce((prev, accu)=> accu+prev,0)===0) return "0";
    
    // 그 외의 경우 자릿수 맞추기
    numbers.sort(function(a,b){
        return parseInt(b.toString().repeat(4).slice(0,4))
            -parseInt(a.toString().repeat(4).slice(0,4));
    });
    return numbers.map(it => it.toString()).join("");
}