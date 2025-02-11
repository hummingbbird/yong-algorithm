function solution(my_string, alp) {
    // 1. map을 이용한 변환
    return [...my_string].map(it=>it===alp?it.toUpperCase():it.toLowerCase()).join("");

    // 2. replaceAll 메소드를 이용한 변환(so easy!!!)
    return my_string.replaceAll(alp, alp.toUpperCase());
}
