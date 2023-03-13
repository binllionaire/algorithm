
const sol = (input) => {
    const [N, M] = input[0].split(' ')
    input = input.slice(1);
    input = input[0].split(' ')
    const tree = new Array();
    let low = 0; 
    
    input.forEach(element => {
        tree.push(Number(element))
    });
    let high = Number(Math.max(...tree))
    
    while(low <= high){
        let mid = parseInt((high+low)/2)
        sum = 0
        tall = tree.map((tree) => {if(tree>mid)sum += tree-mid})
        if(sum >= Number(M)){ //총 높이가 필요한 높이 보다 클때
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

  