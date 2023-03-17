let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");

const N = input.shift()
const myCard = input.shift().split(" ").map((v)=>Number(v)).sort((a, b) => a - b)
const M = input.shift()
const numCard = input.shift().split(" ").map((v)=>Number(v))

var MyCardMap = new Map();

for (number of myCard) {
  if (MyCardMap.has(number))
    MyCardMap.set(number, MyCardMap.get(number) + 1);
  else MyCardMap.set(number, 1);
}

let answer = new Array();
for (number of numCard) {
  if (MyCardMap.has(number)) answer.push(MyCardMap.get(number));
  else answer.push(0);
}
console.log(answer.join(" "))