function solution(n, slicer, num_list) {
    let [a, b, c] = [...slicer]; // array의 원소를 각 변수 a, b, c에 저장
    switch (n) {
        case 1:
            return num_list.slice(0, b+1);
        case 2:
            return num_list.slice(a, num_list.length);
        case 3:
            return num_list.slice(a, b+1);
        case 4:
            return num_list.slice(a, b+1).filter((_, idx) => !(idx % c));
            
    }
}