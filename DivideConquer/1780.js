let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");

const N = input.shift()

let paper = new Array()
for(let i =0;i<N ; i++){
    paper.push(input[i].split(" ").map((v)=>Number(v)))
}
let result = [0,0,0]

// 나누는 함수 (재귀 시작)
function divide(arr) {
    // 예외 : 크키가 1 * 1인 경우
    // 개수 count.
    if (arr.length === 1) {
        result[arr[0][0]+1]++;
    }
  
    // 3 * 3 분할을 위해 3으로 나눈 값을 구함.
    const splitCnt = Math.floor(arr.length / 3);
  
    // 9등분 재귀 시작.
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        const splitArr = [];
  
        // 각 구역의 시작과 끝 위치 파악
        const yStart = splitCnt * i;
        const yEnd = splitCnt * (i + 1);
        const xStart = splitCnt * j;
        const xEnd = splitCnt * (j + 1);
        //console.log(yStart,yEnd,xStart,xEnd)
        // 각 배열의 y축을 위한 변수.
        let col = 0;
  
        // 9등분 배열을 구하고
        for (let y = yStart; y < yEnd; y++) {
          splitArr[col] = [];
  
          for (let x = xStart; x < xEnd; x++) {
            splitArr[col].push(arr[y][x]);
          }
          
          col++;
        }
        
        //console.log(splitArr)
        // 확인해서 모든 원소가 같으면 개수 count
        // 아니면 재귀
        if (checkArr(splitArr, splitCnt)) {
          const val = splitArr[0][0];
          result[val+1]++;
        } else {
          divide(splitArr);
        }
      }
    }
  }
  
  // 배열의 모든 원소가 같은지 확인하는 정복 부분.
  function checkArr(arr, length) {
    let num = arr[0][0];
  
    for (let i = 0; i < length; i++) {
      for (let j = 0; j < length; j++) {
        if (num !== arr[i][j]) {
          return false;
        }
      }
    }
    return true;
  }

if(checkArr(paper,N)){
    let num = paper[0][0]
    result[num+1]++;
}else{
    divide(paper)
}

console.log(result.join("\n"))
