const isPrime = (n) => {
    if (n <= 1) return false;
    if (n === 2) return true;
    for (let i=2;i<n/2+1;i++) {
        if (n % i === 0) return false;
    }
    return true;
};

function solution(numbers) {
    var answer = 0;
    const lst = [];
    const visited = Array(numbers.length).fill(false);
    
    const dfs = (cur, idx) => {
        lst.push(parseInt(cur));
        visited[idx] = true;
        for (let i=0;i<numbers.length;i++) {
            if (visited[i] === false) {
                dfs(cur+numbers[i], i);
            }
        }
        visited[idx] = false
        
    }
    
    for (let i=0;i<numbers.length;i++) {
        dfs(numbers[i],i)
    }
    
    const set = [...new Set(lst)];
    set.forEach((item) => {
        if (isPrime(item)){
            answer++;
        }
    })
    return answer;
    
}