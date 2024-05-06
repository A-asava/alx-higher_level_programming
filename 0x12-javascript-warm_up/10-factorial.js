#!/usr/bin/node

function factorial (num) {
  if (num < 0) {
    return -1;
  }
  if (num === 0 || isNaN(num)) {
    return 1;
  }
  return (num * factorial(num - 1));
}

console.log(factorial(Number(process.argv[2])));
