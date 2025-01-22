function solution(my_string, is_suffix) {
    var answer = false;
    const num = my_string.length - is_suffix.length;
    // 첫번째 접근: my_string 3개씩 잘라서 is_suffix와 비교 -> x
    // for (let i=0;i<num+1;i++) {
    //     const candidate = my_string.substr(i, is_suffix.length);
    //     if (candidate === is_suffix) {
    //         return 1;
    //     }
    // }
    
    // 두 번째 접근: my_string의 접미사를 하나씩 만들고 is_suffix와 비교
    for (let i=0;i<num+1;i++){
        // 0~6, 1~6 근데 길이가 같은 건 하나뿐이잖아 그치. 그럼 
    }
    const suffixLength = is_suffix.length;
    const tmp = my_string.substr(my_string.length-suffixLength, my_string.length);
    return is_suffix === tmp? 1:0;
}