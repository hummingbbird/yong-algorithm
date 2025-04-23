function solution(clothes) {
    var answer = 1;
    var category = {};
    clothes.forEach(it => {
        if(!Object.keys(category).includes(it[1])) {
            category[it[1]] = 1;
        } else {
            category[it[1]] += 1;
        }
    });
    Object.values(category).forEach(it => answer *= (it+1));
    return answer-1;
}