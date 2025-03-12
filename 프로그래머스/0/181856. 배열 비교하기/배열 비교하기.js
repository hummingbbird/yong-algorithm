// option 인자 추가해서 두 배열의 길이가 같은 경우에도 이 함수를 사용할 수 있도록 함!
// 비교 연산 코드의 중복을 줄일 수 있음.
const isSame = (a1, a2, option) => {
    if (option === "reduce") {
        a1 = a1.reduce((accu, item)=>accu+item);
        a2 = a2.reduce((accu, item)=>accu+item);        
    }
    return a1 > a2 ? 1 : a1<a2 ? -1 : 0;
}

function solution(arr1, arr2) {
    return arr1.length!==arr2.length? isSame(arr1.length, arr2.length):isSame(arr1, arr2, "reduce");
}
