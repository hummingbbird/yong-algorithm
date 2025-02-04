function devide(num) {
    let cnt = 0;
    while (num > 1) {
        num = num % 2 === 0? num /= 2:(num-1)/2;
        cnt++;
    }
    return cnt;    
}

function solution(num_list) {
    return num_list.reduce((accu, item) => accu+=devide(item),0);

}