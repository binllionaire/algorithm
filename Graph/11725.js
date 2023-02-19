const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


let input = []
let visited = []
let tree = {}
rl.on('line', (line) => {
    input.push(line)
});

rl.on('close', () => {
    const N = +input.shift();
    const edges = input.map(v => v.split(' ').map(Number));
    const tree = [...Array(N + 1)].map(() => []);
    edges.forEach(([a, b]) => {
    tree[a].push(b);
    tree[b].push(a);
    });
    visited = new Array(N+1).fill(0)
    
    const dfs = (node) => {
        for (value of tree[node]){
            if(visited[value] === 0){
                visited[value] = node
                dfs(value,visited)
            }
        }
      
    };
    dfs(1)
    console.log(visited.slice(2).join("\n"));
    process.exit();
})





