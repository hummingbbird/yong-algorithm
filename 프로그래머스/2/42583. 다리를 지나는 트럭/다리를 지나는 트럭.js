function solution(bridge_length, weight, truck_weights) {
    const bridge = new Array(bridge_length-1).fill(0);
    bridge.push(truck_weights.shift());
    let timer = 1;
    while (!bridge.every(item => item === undefined)) {
        // 일단 shift
        bridge.shift();
        // 새로 들어올 애랑 bridge 합이 weight 넘기면 불가능 -> 걍 하나 밀기만(bridge.shift(); bridge.push(0);
        if (truck_weights[0] + bridge.reduce((accu, cur) => accu+cur, 0) > weight) {
            bridge.push(0);
        }
        else {
            bridge.push(truck_weights.shift());
        }
        timer++;
        // 안 넘기면 bridge.shift(); bridge.push(truck_weights.shift();)
    }
    return timer;
}