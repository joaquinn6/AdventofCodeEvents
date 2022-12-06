var fs = require('fs');
var input=fs.readFileSync(process.cwd()+'/2022/dic06/input.txt').toString();

function includesMoreThanOne(str, array){
  sum = 0;
  array.forEach(letter => {
    if (str == letter){
      sum+=1;
    }
  });
  return sum > 1
}

for (let i = 0; i<=input.length-15; i+=1){
  var array =  input.slice(i, i+14).split('')
  var newArray = array.filter((letter) => includesMoreThanOne(letter, array))
  if (newArray.length == 0){
    console.log(i+14)
    break;
  }
}

