// function solution(order) {
//     return order.reduce((accu, it)=> {
//         if (it.indexOf('cafelatte') !== -1) {
//             return accu + 5000;
//         } else return accu + 4500;
//     },0)
// }

const solution = (order) => order.reduce((accu, it) => accu + (it.includes('latte')? 5000: 4500),0);
