#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    console.log((c.repeat(this.width) + '\n').repeat(this.height - 1) + c.repeat(this.width));
  }
}
module.exports = Square;
