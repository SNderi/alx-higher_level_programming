#!/usr/bin/node

const process = require('process');
const args = process.argv;
const result = parseInt(args[2]);
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
