function solution(sizes) {
    let width = 0;
    let height = 0;
    
    // 더 긴 쪽 width로 통일
    sizes = sizes.map((item) => {
        return item.sort((a, b) => b-a)
    });
    
    sizes.forEach((item) => {
       if (width < item[0]) {
           width = item[0];
       } 
        if (height < item[1]) {
           height = item[1];
       } 
    });
    
    return width * height
    
}