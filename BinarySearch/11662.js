let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");

const [Ax,Ay,Bx,By,Cx,Cy,Dx,Dy] = input.shift().split(" ")

let low = 0; 
let high = 100;
const distance = (t) =>{
    mx = Ax * t + Bx * (1-t)
    my = Ay * t + By * (1-t)
    kx = Cx * t + Dx * (1-t)
    ky = Cy * t + Dy * (1-t)
    return (((kx-mx) ** 2) + ((ky-my)**2)) ** 0.5
}
const threeSearch = (start,end)=>{
    while((end-start)>=1e-9){
        let mid1 = (2*start+end)/3
        let mid2 = (start+2*end)/3
        if(distance(mid1)>distance(mid2)){
            start = mid1
        }
        else end = mid2
    }
    return distance(start)
}

console.log(threeSearch(0,1).toFixed(10))