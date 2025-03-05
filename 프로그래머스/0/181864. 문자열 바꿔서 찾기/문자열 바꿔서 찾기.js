function change(target) {
    return [...target].map(it=>it==="A"? "B":"A").join("")
}

function solution(myString, pat) {
    const changePat = change(pat);
    return myString.indexOf(changePat)>=0?1:0;
}