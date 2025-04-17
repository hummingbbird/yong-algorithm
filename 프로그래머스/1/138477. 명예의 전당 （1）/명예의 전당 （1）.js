function solution(k, score) {
    var answer = [score[0]];
    var cache = [score[0]];
    
    for(let i=1; i<score.length;i++) {
        if (cache.length<k) {
            cache.push(score[i]);
        }
        else { 
            if (cache[cache.length-1] < score[i]) {
                cache.pop();
                cache.push(score[i]);
            }
        }
        cache.sort((a,b)=>b-a);
        answer.push(cache[cache.length-1]);
    }
    return answer;
}