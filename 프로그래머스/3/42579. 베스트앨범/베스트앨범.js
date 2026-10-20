function solution(genres, plays) {
    const lst = {};
    const rank = {};
    
    // 1. {장르: [[idx, 재생횟수], [idx, 재생횟수]] ... } 형태로 정리
    // 동시에 장르 별 재생 횟수 합도 구하기
    for(let i=0;i<genres.length;i++) {
        if (lst[genres[i]]) {
            lst[genres[i]].push([i, plays[i]])
            rank[genres[i]] += plays[i]
        }
        else {
            lst[genres[i]] = [[i, plays[i]]]
            rank[genres[i]] = plays[i]
        }
    }
    
    // 2. 각 장르 별 곡들을 재생 횟수 순으로 정렬
    // (이 때, 위에서 i=0부터 넣어줬기 때문에 자동으로 고유 번호 순 정렬이 되어 있는 상황)
    const tmp = Object.fromEntries(Object.entries(lst).map((item) => {
        return [item[0], item[1].sort((a, b) => { return b[1]-a[1]}).slice(0,2)]
    }));
    
    // 3. rank 객체를 통해 재생횟수 기준으로 정렬된 장르 리스트 추출
    const ranking = Object.entries(rank)
        .sort((a,b) =>  b[1]-a[1])
        .map((item) => {return item[0]});
    
    // 4. 정답 도출
    const answer = [];
    ranking.forEach((item) => {
        tmp[item].forEach((ele) => {
            answer.push(ele[0])
        })
    })
    
    return answer;
}