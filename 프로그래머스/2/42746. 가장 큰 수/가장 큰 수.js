function solution(numbers) {
    // 모두 0인 경우 "0" 리턴
    if (numbers.reduce((prev, accu)=> accu+prev,0)===0) return "0";
    
    // 그 외의 경우 자릿수 맞추기
    numbers.sort(function(a,b){
        const paddedB = parseInt(b.toString().repeat(4).slice(0,4))
        const paddedA = parseInt(a.toString().repeat(4).slice(0,4));
        if (paddedB===paddedA) return b-a;
        else return paddedB - paddedA;
    });
    return numbers.map(it => it.toString()).join("");
}