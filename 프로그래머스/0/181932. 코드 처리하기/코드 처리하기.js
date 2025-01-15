function solution(code) {
    var ret = '';
    var mode = 0;
    [...code].forEach((it, idx)=> {
        if (mode==0) {
            if (code[idx]!=="1" && idx%2==0) {
                ret += code[idx]
            }
            else if (code[idx]==1){
                mode = 1;
            }
        }
        else {
            if (code[idx]!=="1" && idx%2==1) {
                ret += code[idx]
            }
            else if (code[idx]==1){
                mode = 0;
            }
        }
    // console.log("code[i]: ", code[idx], "ret: "+ret+ ", mode: "+mode);
    })
    return ret.length==0? "EMPTY":ret;
}