function solution(myStr) {
    var answer = myStr;
    ["a","b","c"].forEach(it=>answer = answer.replaceAll(it,"1"));
    answer = answer.split("1").filter(it => it !== ""); 
    return answer.length!==0? answer:["EMPTY"];
}