let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N,M] = input.shift().split(" ")
const [...A] =  input.shift().split(" ").map((v)=>Number(v))
const [...B] = input.shift().split(" ").map((v)=>Number(v))
console.log([...A,...B].sort((a, b) => a - b).join(" "))
