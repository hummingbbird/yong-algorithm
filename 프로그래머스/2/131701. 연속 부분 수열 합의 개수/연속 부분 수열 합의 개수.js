function solution(elements) {
    var answer = new Set();
    var circle = elements.concat(elements);
    for(let i=1;i<=elements.length;i++) {
        for(let j=0;j<elements.length;j++) {
            answer.add(circle.slice(j, j+i).reduce((accu,it)=>accu+it, 0));
        }
    }
    return [...answer].length;
}