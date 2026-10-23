function solution(id_list, report, k) {
    let answer = [];
    let singo = {}; // 피신고자:[신고자명단]
    let message = {};
    id_list.forEach((item) => {
        singo[item] = [];
        message[item] = 0;
    });
    
    report.forEach((item) => {
        const [victim, p] = item.split(' ');
        singo[p].push(victim);
    })
    
    singo = Object.entries(singo).map((item) => {
        const set = new Set(item[1]);
        return [item[0], [...set]];
    })
    // item[1].length >= k 이면 신고 당함요.
    singo.forEach((item) => {
        if (item[1].length >= k) {
            item[1].forEach((item) => message[item] += 1);
        }
    })
    return Object.values(message);
}