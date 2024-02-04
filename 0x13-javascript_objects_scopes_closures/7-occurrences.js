#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((v) => v === searchElement).length;
};
