function solution(myString, pat) {
    var patIdx = myString.lastIndexOf(pat);
    return myString.slice(0, patIdx+pat.length);
}