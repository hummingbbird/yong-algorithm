function solution(prices) {
    // 그러게 생각해보니까 끝까지 상승만 하면 굳이 이걸 다 검사할 필요가 없잖음.
    // 그래프가 감소하는 때 검사
    const prices_length = prices.length;
    const stack = [];
    const ans = [];
    for (let i=0;i<prices_length;i++) {
        ans.push(prices_length-i-1);
    }
    
    for (let i=0;i<prices_length-1;i++) {
        stack.push([i,prices[i]]);
        if (prices[i] > prices[i+1]) {
            while (stack.length !== 0 && stack.at(-1)[1] > prices[i+1]) {
                const tmp = stack.pop();
                ans[tmp[0]] = (i+1)-tmp[0];
            }
        }
    }
    
    return ans;
}