function solution(d, budget) {
    var answer = d.length;
    d.sort(function(a,b){ return a-b});
    for(let i=0;i<d.length+1;i++) {
        if (d.slice(0, i).reduce((accu, item)=>accu+item,0) > budget) {
            return i-1;
        };
    }
    return answer;
}