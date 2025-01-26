function solution(arr) {
    var answer = [];
    let twos=[];
    // item=2인 원소들의 index 모두 저장
    arr.forEach((item, i)=> {
        if(item==2) twos.push(i);
    })
    switch (twos.length) {
        case 0: return [-1];
        case 1: return [2];
        default:
            console.log("twos: "+twos, "twos's length:"+twos.length);
            const lastIdx = twos.length;
            for (let i=twos[0]; i<=twos[lastIdx-1];i++) {
                answer.push(arr[i]);
            }
    } 
    return answer;
}