const isRightPassword = (s) => {
    // 3~15자 / 소문자 / - _ .만 가능 / .는 양 끝에 사용 x, 연속 x
    const pattern = /^[a-z0-9_.-]$/;
    if (s.length<3 || s.length>15) return false;
    else if (pattern.test(s) && s.indexOf("..") !== -1 && s[0] !== "." && s[s.length-1] !== ".") {
        return false;
    }
    return true;
}

const convertor = (s) => {
    s = s.toLowerCase(); // 1단계
    s = s.replace(/[^a-z0-9_.-]/g, "");// 2단계
    s = s.replace(/\.{2,}/g, "."); // 3단계
    s = s.replace(/^\.|\.$/, ""); // 4단계
    if (s === "") s = "a"; // 5단계
    if (s.length>=16) s = s.slice(0, 15); // 6단계
    s = s.replace(/\.$/g, "");
    while (s.length <= 2) s+= s.slice(-1); //7단계
    return s
};

function solution(new_id) {
    return convertor(new_id);
}