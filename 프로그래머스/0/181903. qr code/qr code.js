function solution(q, r, code) {
    var answer = '';
    for (let i=r;i<code.length;i+=q) {
        answer += code[i];
    }
    return answer;
    return [...code].filter((_, i) => i % q === r).join('');
    // code에서 index를 q로 나눈 나머지가 r인 애들만 남아서 array가 되는데 그걸 join하니까 ... 와 개쩌는 코드다 !
}