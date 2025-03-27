function solution(rank, attendance) {
    var answer = 0;
    var lst = [];    
    rank.forEach((it, index)=>{
      if(attendance[index]) {
        lst.push({name: index, rank: it});
        };
    });
    // rank 기준으로 상위 3개 뽑아서 연산해서 return
    lst = lst.sort(function(a, b){ return a.rank-b.rank}).slice(0,3);
    return (lst[0].name * 10000) + (lst[1].name * 100) + lst[2].name;
}