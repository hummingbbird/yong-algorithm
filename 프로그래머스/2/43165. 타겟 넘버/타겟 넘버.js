function solution(numbers, target) {
    var ans = 0;
    let cur = 0;
    
    const dfs = (cur_res, i) => {
        const minus = cur_res - numbers[i];
        const maxi = cur_res + numbers[i];
        i++;
        if (i > numbers.length) {
            if (target === cur_res) {
                ans++;
            }
            return;
        }
        dfs(minus, i);
        dfs(maxi, i);
    };
    
    dfs(0, 0)
    return ans;
}