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

function calculateEscenario(hight, indexes = []){
  let back = 0
  for(let i = indexes[0]-1; i >=0; i-=1){
    if (matriz[indexes[1]][i] >= hight){
      back += 1;
      break
    }
    back += 1;
  }

  let forward = 0
  for(let i = indexes[0]+1; i <=xMaxIndex; i+=1){
    if (matriz[indexes[1]][i] >= hight){
      forward +=1;
      break
    }
    forward +=1;
  }

  let up = 0
  for(let i = indexes[1]-1; i >=0; i-=1){
    if (matriz[i][indexes[0]] >= hight){
      up += 1;
      break
    }
    up += 1;
  }
  let down = 0
  for(let i = indexes[1]+1; i <=yMaxIndex; i+=1){
    if (matriz[i][indexes[0]] >= hight){
      down += 1;
      break
    }
    down+=1;
  }
  return up * down * forward * back;
}

let maxEscenario = 0;
matriz.forEach((line, indexY) => {
  line.forEach((tree, indexX) => {
    let escenario = calculateEscenario(tree, [indexX, indexY])
    if (escenario > maxEscenario){
      maxEscenario = escenario;
    }
  });
});

console.log(maxEscenario);