function solution(n, times) {
    var answer = 0;
    // 음.. 뭘까? 큐가 아니라고?
    const max = Math.max(...times) * n;
    
    let l = Math.min(...times);
    let r = Math.max(...times) * n;
    
    while (l < r) {
        const mid = Math.floor((l+r)/2);
        let p = 0;
        times.forEach((item) => {p+=Math.floor(mid/item)});
        
        if (p < n) {
            l = mid+1;
        }
        else {
            r = mid;
        }
    };
    return l;
}