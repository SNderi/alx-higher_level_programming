#!/usr/bin/node

const process = require('process');
const args = process.argv;

function factorial (a) {
  if (a === 0 || Number.isNaN(a)) {
    return (1);
  }
  return (a * factorial(a - 1));
}

const result = factorial(parseInt(args[2]));
console.log(result);
