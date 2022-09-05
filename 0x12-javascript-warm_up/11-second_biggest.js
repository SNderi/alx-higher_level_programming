#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const numList = [];
  for (const num of args) {
    if (!isNaN(num)) {
      numList.push(parseInt(num));
    }
  }
  numList.sort(function (a, b) { return b - a; });
  console.log(numList[1]);
}
