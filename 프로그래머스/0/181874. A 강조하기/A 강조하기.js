function solution(myString) {
    return [...myString].map((it)=>(it==="a" || it==="A")?it.toUpperCase():it.toLowerCase()).join("");
}