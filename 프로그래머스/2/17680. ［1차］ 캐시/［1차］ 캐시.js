function solution(cacheSize, cities) {
    if(cacheSize===0) return 5*(cities.length);
    var cacheLst = []; // 최근사용 --- 과거사용 순서로 삽입
    var answer = 0;
    cities.forEach((item, i)=>{
        const it = item.toLowerCase();
        if(cacheLst.includes(it)) { // cache hit
            answer+=1;
            cacheLst = cacheLst.filter(ele => ele !== it);
            cacheLst.splice(0, 0, it);
        } else if (cacheLst.length < cacheSize){ // cache miss + 빈자리 o
            cacheLst.splice(0, 0, it);
            answer+=5;
        } else { // cache miss + 빈자리 x
            cacheLst.pop();
            cacheLst.splice(0, 0, it);
            answer+=5;
        }
        // console.log(cacheLst);
    })
    return answer;
}