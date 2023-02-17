const readline = require("readline");
const { arrayBuffer } = require("stream/consumers");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


let input = []
let tree = {}
rl.on('line', (line) => {
    input.push(line)
});
 
rl.on('close', () => {
    let n = input[0]
    input = input.splice(1)
    for(let i =0; i<n; i++){
        const [node,left,right] = input[i].split(' ')
        tree[node] = [left,right];
    }
    preorder("A")
    inorder("A")
    postorder("A")

    console.log(pre_result)
    console.log(in_result)
    console.log(post_result)
    process.exit();
})

let pre_result = ""
let in_result = ""
let post_result = ""

const preorder = (node) => { // 전위순회 : 재귀의 맨앞에서 기록
    if(node === ".") return
    const [lt, rt] = tree[node]
    pre_result += node
    preorder(lt)
    preorder(rt)
}

const inorder = (node) => { // 중위순회 : 왼쪽 재귀 끝나면 기록
    if (node === ".") return;
    const [lt, rt] = tree[node];
    inorder(lt);
    in_result += node;
    inorder(rt);
  }

const postorder = (node) => { //후위순회 : 재귀 끝나면 기록
    if (node === ".") return;
    const [lt, rt] = tree[node];
    postorder(lt);
    postorder(rt);
    post_result += node;
}