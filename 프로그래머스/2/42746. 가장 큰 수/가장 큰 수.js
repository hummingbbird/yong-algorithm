function solution(numbers) {
    const maximum = numbers.sort((a, b) => 
                        parseInt(String(b) + String(a)) - parseInt(String(a) + String(b))
                        ).join('');
    return maximum[0] === "0" ? "0": maximum;
}