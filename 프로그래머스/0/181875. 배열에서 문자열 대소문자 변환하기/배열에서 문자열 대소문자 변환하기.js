function solution(strArr) {
    return strArr.map((it,i)=>{
        return (i%2==0)? it.toLowerCase():it.toUpperCase();
    });
}