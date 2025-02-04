function solution(num_list) {
    if (num_list.length>=11) return num_list.reduce((accu, item)=> accu+item, 0);
    else return num_list.reduce((accu, item)=> accu*item, 1);
}

// 조건문을 삼항 연산자로 바꿔 reduce문 안으로 넣어줄 수도 있음
// 코드가 더 간결해짐
function solution2(num_list) {
    return num_list.reduce((a, e)=> num_list.length>10? a+e:a*e);
}
