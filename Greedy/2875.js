let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");
let [N,M,K] = input[0].split(" ")


let girlsTeam = parseInt(N/2)
let boysTeam = M
let team = Math.min(girlsTeam,boysTeam)
let leftGirls = N-(2*team)
let leftBoys = M-team

if(leftGirls+leftBoys < K){
    if(K<=3) team -= 1
    else{
        K = K-(leftBoys+leftGirls)
        if(K%3 == 0)team = team - parseInt(K/3)
        else team = team - (parseInt(K/3) + 1)
    }
}
console.log(team)


