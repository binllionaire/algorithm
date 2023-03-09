
const sol = (input) => {
    const [K, N] = input[0].split(' ')
    input = input.slice(1);
    const lan = new Array();
    
    let low = 1; 
    
    input.forEach(element => {
        lan.push(Number(element))
    });

    let high = Math.max(...lan)
    
    while(low <= high){
        let mid = parseInt((high+low)/2)
        pieces = lan
        .map((lan) => parseInt(lan/mid))
        .reduce((a,b)=>a+b,0); //각각의 랜선을 mid만큼으로 잘랐을 때의 몫을 다 더한 값
        if(pieces >= N){
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return high; 
  };

  const input = [];
  require("readline")
    .createInterface(process.stdin, process.stdout)
    .on("line", (line) => {
      input.push(line);
    })
    .on("close", () => {
      console.log(sol(input));
      process.exit();
    });

  