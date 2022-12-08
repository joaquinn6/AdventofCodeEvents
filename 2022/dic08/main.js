let fs = require('fs');
let matriz = []
let inputArray=fs.readFileSync(process.cwd()+'/2022/dic08/input.txt').toString().split("\n");

inputArray.forEach((line) => {
  let numberLine = []
  line = line.split('');
  line.forEach((strNumber) => {
    numberLine.push(parseInt(strNumber));
  })
  matriz.push(numberLine);
})
const yMaxIndex = matriz.length -1;
const xMaxIndex = matriz[0].length -1;

let visibles = 0;

function isVisible(hight, indexes = []){
  if (indexes.includes(0) || indexes[0] == xMaxIndex || indexes[1] == yMaxIndex){
    return true;
  }
  let back = true
  for(let i = indexes[0]-1; i >=0; i-=1){
    if (matriz[indexes[1]][i] >= hight){
      back = false
      break
    }
  }
  if (back) {
    return true;
  }

  let forward = true
  for(let i = indexes[0]+1; i <=xMaxIndex; i+=1){
    if (matriz[indexes[1]][i] >= hight){
      forward = false
      break
    }
  }
  if (forward) {
    return true;
  }

  let up = true
  for(let i = indexes[1]-1; i >=0; i-=1){
    if (matriz[i][indexes[0]] >= hight){
      up = false
      break
    }
  }
  if (up) {
    return true;
  }
  let down = true
  for(let i = indexes[1]+1; i <=yMaxIndex; i+=1){
    if (matriz[i][indexes[0]] >= hight){
      down = false
      break
    }
  }
  if (down) {
    return true;
  }
  return false;
}

matriz.forEach((line, indexY) => {
  line.forEach((tree, indexX) => {
    if (isVisible(tree, [indexX, indexY])){
      visibles += 1;
    }
  });
});

console.log(visibles);