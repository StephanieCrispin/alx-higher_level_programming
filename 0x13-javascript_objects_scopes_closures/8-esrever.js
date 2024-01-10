#!/usr/bin/node
exports.esrever = function (list) {
  let Arr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    Arr.push(list[i]);
  }
  return Arr;
};
