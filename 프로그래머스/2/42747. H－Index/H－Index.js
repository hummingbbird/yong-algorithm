function solution(citations) {
    const n = citations.length;
    let h = n;
    while (h<=n) {
        if (citations.filter(it => it >= h).length >= h) return h
        else h--;
    }
    return h;
}