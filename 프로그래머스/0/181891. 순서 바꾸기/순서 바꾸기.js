function solution(num_list, n) {
    const front = num_list.slice(n);
    return front.concat(num_list.slice(0,n));
}