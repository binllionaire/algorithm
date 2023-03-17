let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = input.shift()
const myCard = input.shift().split(" ").map((v)=>Number(v)).sort((a, b) => a - b)
const M = input.shift()
const numCard = input.shift().split(" ").map((v)=>Number(v))

const binary_search = (my,num,start,end) =>{
    while (start <= end){
        let mid = parseInt((start+end)/2)
        if(my[mid]===num){
            return true
        }
        else if(my[mid]>num){
            end = mid - 1
        }
        else{
            start = mid + 1
        } 
    }
    return false
}
let result = new Array();
for(let i =0;i<M;i++){
    if(binary_search(myCard,numCard[i],0,N-1)){
        result += "1 "
    }
    else{
        result += "0 "
    }
}
console.log(result)