function solution(food) {
    var answer = '';
    for(let i=1;i<food.length;i++) {
        const foodCount = food[i]/2;
        answer+=(foodCount !== 0)?`${i}`.repeat(foodCount):"";
    }
    return answer+"0"+([...answer].reverse().join(""));
}