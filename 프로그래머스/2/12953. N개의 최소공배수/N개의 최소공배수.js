function solution(arr) {
    var r=1;
    while (true) {
        const tmp = arr.reduce((accu, it)=>accu+r%it,0);
        if (tmp===0){
            break;
        };
        r++;
    }
        
    return r;
}