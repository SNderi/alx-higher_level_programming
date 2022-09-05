#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!isNaN(args[2])) {
  const size = parseInt(args[2]);
  let row = 0;
  while (row < size) {
    let i = 0;
    let col = '';
    while (i < size) {
      col = col + 'X';
      i++;
    }
    console.log(col);
    row++;
  }
} else {
  console.log('Missing size');
}
