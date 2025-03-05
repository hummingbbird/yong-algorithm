function solution(rny_string) {
    var answer="";
    [...rny_string].forEach(it=>it==="m"? answer+="rn":answer+=it); 
    return answer;
}