let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");
let arr = input[0].split("")
arr = arr.map(v=>parseInt(v))
let sum =0;
arr.map(v=>sum=sum+v)
if(sum%3 !=0){
    console.log(-1)
}
else if(arr.indexOf(0)<0){
    console.log(-1)
}
else{
    console.log(arr.sort((a,b)=>b-a).join(""))
}
