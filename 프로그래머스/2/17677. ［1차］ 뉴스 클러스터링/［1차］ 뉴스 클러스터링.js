// 다중집합 생성 함수
const multiset = (s) => {
    let ms = [];
    for(let i=0;i<s.length-1;i++) {
        const part = s.slice(i,i+2);
        if(part.match(/[^a-z]/g)===null) ms.push(part);
    }
    return ms;
}

function solution(str1, str2) {    
    // 1. 다중집합 생성
    var multiset1 = multiset(str1.toLowerCase());
    var multiset2 = multiset(str2.toLowerCase());
    
    // 2. 합집합과 교집합 구하기
    var inter = []; // 교집합
    multiset1.forEach(it=> {
        if (multiset2.includes(it)) {
            inter.push(it);
            multiset2.splice(multiset2.indexOf(it),1);
        } else {
            
        }
    });
    
    var union = multiset1.concat(multiset2); // 합집합
    
    return (union.length===0 && inter.length===0)?
    65536
    :Math.floor((inter.length/union.length)*65536);
}