const changeToBin = (nums) => {
    const arr = [];
    nums.forEach((item) => {
        const tmp = item.toString(2);
        const tmp_arr = Array(nums.length - tmp.length).fill("0").join("")+tmp;
        arr.push([...tmp_arr]);
    })
    return arr;
}

const decrypt = (arr1, arr2) => {
    const N = arr1.length;
    const ans = [];
    for (let i=0;i<N;i++) {
        const tmp = [];
        for (let j=0;j<N;j++){
            if (arr1[i][j] === "1" || arr2[i][j] === "1") {
                tmp.push("#");
            }
            else {
                tmp.push(" ");
            }
        }
        ans.push(tmp.join(""));
    }
    return ans;
};

function solution(n, arr1, arr2) {
    var answer = [];
    // arr1 지도 && arr2 지도 비트맵 연산 후 결과 #으로 변환하여 반환
    return decrypt(changeToBin(arr1), changeToBin(arr2));
}