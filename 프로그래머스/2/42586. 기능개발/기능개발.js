const getDeploy = (p, s) => {
  let cnt = 0;
  while (p < 100) {
      p+= s;
      cnt += 1;
  };
  return cnt;
};

function solution(progresses, speeds) {
    var deploys = [];
    
    // 1. 배포까지 걸리는 시간 계산
    for (let i=0;i<speeds.length;i++) {
        const deploy = getDeploy(progresses[i], speeds[i]);
        
        if (i !== 0 && deploys[deploys.length-1] >= deploy) {
            deploys.push(deploys[deploys.length-1]);
        } else {
            deploys.push(deploy);
        }
    };
    
    // 최종 출력
    var answer = [];
    Array.from(new Set(deploys)).map(it => {
        answer.push(deploys.filter(d => d === it).length);
    });
    
    return answer;
}