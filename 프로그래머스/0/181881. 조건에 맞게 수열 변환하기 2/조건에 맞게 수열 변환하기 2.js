function convertArr(arr) {
    return arr.map((it) => {
        if (it >= 50 && it%2===0) return it/2;
        if (it < 50 && it%2!==0) return (it*2)+1;
        return it;
    });
}

function solution(arr) {
    let newArr = arr;
    let i=0;
    while (true) {
        if (newArr.toString() == convertArr(newArr).toString()) break;
        else {
            i++;
            newArr = convertArr(newArr);
        }
    }

    
    return i;
}
