const solution = (myString) => {
    return [...myString].map(it => 'abcdefghijk'.includes(it)? "l":it).join("");
}