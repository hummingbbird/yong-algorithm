function solution(N, stages) {
    userNum = stages.length;
    var answer = [];
    for(let i=1;i<N+1;i++) {
        const failure = (stages.filter(it=>it === i).length)/(stages.filter(it => it >= i).length);
        answer.push({index: i, value: failure});
    }
    // 정렬
    answer = answer.sort((a, b) => {
      if (b.value !== a.value) {
        return b.value - a.value; // 점수는 내림차순 정렬
      } else {
        return a.index - b.index; // 같을 경우 오름차순으로
      }
    }).map(it => it.index);
    return answer;
}