function solution(citations) {
    const n = citations.length;
    let answer = 0;
    for (let i=0;i<=n;i++) {
        const underH = citations.filter((item) => item < i);
        if ((n-underH.length)>=i && underH.every((item)=>item<=i)) {
            answer = i;
        }
    }
    return answer;
}