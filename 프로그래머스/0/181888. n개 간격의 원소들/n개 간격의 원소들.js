function solution(num_list, n) {
    return num_list.filter((item, i)=> i%n==0);
}