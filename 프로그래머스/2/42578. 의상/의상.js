function solution(clothes) {
    const dic = {};
    clothes.forEach((item) => {
        if (dic[item[1]]) {
            dic[item[1]] += 1;
        }
        else {
            dic[item[1]] = 2;
        }
    })
    return Object.values(dic).reduce((prev,item) => prev*item)-1;
}