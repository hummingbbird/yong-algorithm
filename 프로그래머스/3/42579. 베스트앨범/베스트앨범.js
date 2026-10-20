function solution(genres, plays) {
    const lst = {};
    const rank = {};
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
    const tmp = Object.fromEntries(Object.entries(lst).map((item) => {
        return [item[0], item[1].sort((a, b) => { return b[1]-a[1]}).slice(0,2)]
    }));
    
    const ranking = Object.entries(rank)
        .sort((a,b) =>  b[1]-a[1])
        .map((item) => {return item[0]});
    
    const answer = [];
    
    ranking.forEach((item) => {
        tmp[item].forEach((ele) => {
            answer.push(ele[0])
        })
    })
    
    return answer;
}