const isRight = (s) => {
    if (s.length < 2) return false;
    const s_lst = [...s];
    const q = [s_lst.shift()];
    for (let i=0; i<s_lst.length;i++) {
        if (s_lst[i] === "(") {
            q.push("(");
        } else if (q[q.length-1] === "(") {
            q.pop();
        }
    }
    return (q.length === 0)
};

const divider = (s) => {
    // w를 u(균형), v로 분리
    // i를 2부터 늘려가면서 s_lst[0:i]의 (와 )개수 세서 같으면 리턴
    for (let i=2;i<=s.length;i++) {
        const left = s.slice(0, i);
        if ([...left].filter((item) => item === "(").length === [...left].filter((item) => item === ")").length) {
            return [left, s.slice(i)]
        }
    }
    return ["", s]
}

const reverser = (s) => {
    let ans = "";
    [...s].forEach((item) => {
        if (item === "(") ans+= ")";
        else ans+="(";
    })
    return ans;
}

const convertor = (w) => {
    if (isRight(w) || w==="") return w;
    // w를 u(균형), v로 분리
    let [u, v] = divider(w);
    if(isRight(u)) { 
        v = convertor(v);
        return u + v;
    }
    else {
        v = convertor(v);
        let tmp = "(" + v + ")";
        tmp += reverser(u.slice(1, u.length-1));
        return tmp;
    }
}

function solution(p) {
    return convertor(p);
}