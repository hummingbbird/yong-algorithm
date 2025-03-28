function solution(str_list, ex) {
    return str_list.filter(it => it.indexOf(ex) === -1).join("");
}