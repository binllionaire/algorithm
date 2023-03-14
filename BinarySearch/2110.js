
    let fs = require("fs");
    let input = fs.readFileSync("input.txt").toString().trim().split("\n");
    
    const [N, C] = input
    .shift()
    .split(" ")
    .map((v) => Number(v));
    let house = input.map((v) => Number(v)).sort((a, b) => a - b);
    let low = 1; 
    let high = house[house.length-1]
    while(low <= high){
        let mid = parseInt((high+low)/2)
       
        let current  = house[0]
        count =1
        for(let i=0;i<house.length;i++){
            if(house[i]>=current+mid){ //공유기 설치할 집이 현재 집으로 부터의 거리간격과 같거나 먼곳에 위치한다면
                count += 1 
                current = house[i] //현재 집 갱신
            }
        }
        if(count >= Number(C)){ //공유기 설치한 집이 원하는 개수보다 크다면
             low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    console.log(high)
    return high; 



  