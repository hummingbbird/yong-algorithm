function solution(numbers) {
    if (numbers.reduce((prev, accu)=> accu+prev,0)===0) return "0";
    numbers.sort(function(a,b){
        if (parseInt(b.toString().repeat(4).slice(0,4)) === parseInt(a.toString().repeat(4).slice(0,4))) return b-a;
        else {
            return parseInt(b.toString().repeat(4).slice(0,4)) - parseInt(a.toString().repeat(4).slice(0,4));
        }
    });
    return numbers.map(it => it.toString()).join("");
}