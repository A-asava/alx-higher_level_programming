#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arg = process.argv.slice(2).map(Number);
  const arr = arg.sort(function (a, b) { return b - a; });
  const secondLargest = arr[1];
  console.log(secondLargest);
}
