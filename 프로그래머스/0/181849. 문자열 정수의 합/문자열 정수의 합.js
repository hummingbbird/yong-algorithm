function solution(num_str) {
    return [...num_str].map(it=>parseInt(it)).reduce((it, accu) => it + accu);
}