#!/usr/bin/node

const arg = process.argv;

if (isNaN(arg[2]) || arg[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < arg[2]; x++) {
    console.log('C is fun');
  }
}
