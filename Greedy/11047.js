let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");

let [N,K] = input.shift().split(" ")
const unit = new Array()
input.map((v)=>unit.push(v))
let coin = 0
for(let i=unit.length;i>=0;i--){
    const temp = parseInt(K/unit[i])
    if(temp>0){
        coin += temp
        K = K-(temp*unit[i])
    }
}
console.log(coin)
