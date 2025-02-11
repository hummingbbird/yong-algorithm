function solution(strArr) {
    return strArr.map((it,i)=>(i%2==0)? it.toLowerCase():it.toUpperCase());
}
