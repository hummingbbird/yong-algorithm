const findYaksu = (n) => {
    const ans = [];
    for(let i=3;i<n/2;i++){
        if (n%i === 0) {
            ans.push(i);
        }
    }
    return ans;
}

function solution(brown, yellow) {
    const rec = brown + yellow;
    const hubo = findYaksu(rec);
    let ans = [];
    hubo.forEach((item) => {
        const w = item;
        const h = rec/item;
        if (brown === ((2*w) + (2*h) - 4)) {
            ans = [w, h];
        }
    })
    
    return ans;
}