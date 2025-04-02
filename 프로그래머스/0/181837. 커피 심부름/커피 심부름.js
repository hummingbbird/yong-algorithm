function solution(order) {
    return order.reduce((accu, it)=> {
        if (it.indexOf('cafelatte') !== -1) {
            return accu + 5000;
        } else return accu + 4500;
    },0)
}