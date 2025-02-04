function solution(num_list) {
    if (num_list.length>=11) return num_list.reduce((accu, item)=> accu+item, 0);
    else return num_list.reduce((accu, item)=> accu*item, 1);
}