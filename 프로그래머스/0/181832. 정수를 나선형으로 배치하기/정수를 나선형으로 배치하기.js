function solution(n) {
    var answer = [];
    // 0으로 2차원 배열 만들어주기
    for(let i=0;i<n;i++) {
        answer.push(new Array(n).fill(0));
    }
    // 필요한 변수들 정리
    var num = 1; // 배열에 들어갈 숫자 
    var i=0, j=0;
    var trigger = n; // 주기가 돌아가는 기준이 되는 숫자
    var flag = 1; // 주기 내에서 4단계로 구분됨
    while(num <= n*n) {
      switch(flag) {
        case 1:
          while (j < trigger) {
            answer[i][j] = num;
            num++;
            j++;
          }
          j--;
          flag++;
          i++;
          break;
        case 2:
          while (i < trigger) {
            answer[i][j] = num;
            num++;
            i++;
          }
          i--;
          flag++;
          j--;
          break;
        case 3:
          while (j >= n-trigger) {
            answer[i][j] = num;
            num++;
            j--;
          }
          j++;
          flag++;
          i--;
          break;
        case 4:
          while (i >= n-trigger+1) {
            answer[i][j] = num;
            num++;
            i--;
          }
          i++;
          flag=1;
          j++;
          trigger--;
          break;
      }
    }
    return answer;
}