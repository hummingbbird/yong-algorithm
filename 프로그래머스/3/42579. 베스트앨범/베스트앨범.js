function solution(genres, plays) {
    const play = {};
    const list = [];
    for(let i=0;i<genres.length;i++){
        // 1. 장르별 play수 누적
        if (play[genres[i]]) {
            play[genres[i]] += plays[i];
        } 
        else {
            play[genres[i]] = plays[i];
        }
        list.push([i, genres[i], plays[i]])
    }
    // 2. 장르 정렬 먼저
    
    return list.sort((a, b) => {
        return b[2]-a[2];
    })
    
    // 3. 그러면 이 (고유번호, 장르, 재생회수) 형태의 배열을 장르 순, 재생회수, 고유번호 순으로 정렬하면 안 됨?
}