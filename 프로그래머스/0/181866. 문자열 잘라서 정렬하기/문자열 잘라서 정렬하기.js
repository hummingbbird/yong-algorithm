function solution(myString) {
    return myString.split("x").filter(it=>it!=="").sort();
}