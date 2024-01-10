#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      c === undefined
        ? console.log('X'.repeat(this.width))
        : console.log(c.repeat(this.width));
    }
  }
};
