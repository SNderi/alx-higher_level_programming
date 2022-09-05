#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!isNaN(args[2])) {
  const limit = parseInt(args[2]);
  let i = 0;
  while (i < limit) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
