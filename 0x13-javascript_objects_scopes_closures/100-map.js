#!/usr/bin/node

const list = require('./100-data').list;

const arr = list.map((elem, idx) => elem * idx);

console.log(list);
console.log(arr);
