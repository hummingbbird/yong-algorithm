const isSame = (a1, a2) => {
    if (a1 === a2) return 0;
    else if (a1 < a2) return -1;
    else return 1;
}

function solution(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return arr1.length > arr2.length?1:-1;
    } else {
        return isSame(arr1.reduce((accu, item)=>accu+=item), arr2.reduce((accu, item)=>accu+=item));
    }
}