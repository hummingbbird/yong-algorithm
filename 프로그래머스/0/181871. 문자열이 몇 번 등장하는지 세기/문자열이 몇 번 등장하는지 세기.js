function solution(myString, pat) {
    let answer = 0;
    const lastIdx = myString.length - pat.length+1;
    for(let i=0;i<lastIdx;i++){
        if (myString.slice(i, i+pat.length) === pat) answer+=1;
    }
    
    return answer;
    
}