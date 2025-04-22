// discount에서 10일씩 slice 후 want와 비교
// want의 item 개수를 count해서 number와 같을 경우 합해주기
// 총합 curCount가 10이라면 +=1

function solution(want, number, discount) {
  var answer = 0;
  for(let i=0;i<discount.length-10+1;i++){
    const curDiscount = discount.slice(i, i+10);
    const curCount = want.reduce((accu, item, i)=> {
      if(curDiscount.filter(it=>it === item).length === number[i]){
        return accu+number[i];
      }
    },0);
      
    answer += curCount===10? 1:0;
    };
    return answer;
};