function solution(my_string, alp) {
    return [...my_string].map(it=>it===alp?it.toUpperCase():it.toLowerCase()).join("");
}