function solution(number) {
    return [...number].reduce((prev, item)=> prev+Number(item), 0)%9;
}