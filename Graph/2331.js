const readline = require("readline");
const { arrayBuffer } = require("stream/consumers");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let A,P;

rl.on("line", (line) => {
    input = line.split(' ').map(el => parseInt(el)); // 1 2 3 4
    rl.close();
});
 
rl.on('close', () => {
    A = input[0]
    P = input[1]
    Sequence()
    process.exit();
})

const Sequence = () => {
    let D = [A]
    while(1){
        A = NumSquare(A)
        D.push(A)
        check = new Set(D)
        if(D.length != check.size){
            break
        }
    }
    D.splice(D.indexOf(D[D.length-1]))
    console.log(D.length)
}

const NumSquare = (num) => {
    let nums = [];
    do{
        nums.push(num%10);
        num = Math.floor(num/10)
    }while(num>0)

    let sum = 0;
    for(var i=0;i<nums.length;i++){
        sum += nums[i] ** P
    }
    return sum
}
