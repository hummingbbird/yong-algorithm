function solution(a, b, c, d) {
    const maxValue = Math.max(a,b,c,d);
    const minValue = Math.min(a,b,c,d);
    
    const arr=[a,b,c,d];
    const maxCount = arr.filter(element=>element==maxValue).length;
    const minCount = arr.filter(element=>element==minValue).length;
    
    if (maxCount == minCount) {
        switch (maxCount) {
            case 4: return 1111*a; // 3333
            case 1: 
                // 1234랑 1224를 구분해야함
                const set = new Set(arr);
                if (set.size==4) {
                    return minValue;
                } else {
                    // 1224의 경우, minCnt=1, maxCnt=1, 
                    const same = arr.filter(item => item!=maxValue && item!=minValue)[0];
                    // return arr.reduce((prev, item)=> {if(same==item) prev*item});
                    return arr.filter(item=>item!==same).reduce((prev,item)=> prev*item, 1);
                }
            case 2: return (maxValue+minValue) * Math.abs(maxValue-minValue); // 1122
        }
    } else if (maxCount+minCount==4) {
        return maxCount==3? ((10*maxValue)+minValue)**2:((10*minValue)+maxValue)**2;
    } else {
        // 1123, 1344의 경우만 존재(min이 2개거나 max가 2개거나)
        const same = maxCount==2? maxValue:minValue;
        return arr.filter(item=>item!==same).reduce((prev,item)=> prev*item, 1);
    }
}