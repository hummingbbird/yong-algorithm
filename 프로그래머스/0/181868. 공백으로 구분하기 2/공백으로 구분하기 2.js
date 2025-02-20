function solution(my_string) {
    const char = my_string.split(" ");
    return char.filter(it=>it!=="");
} 