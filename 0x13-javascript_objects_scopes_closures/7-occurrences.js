#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const lis = [];
  for (const elem of list) {
    if (elem === searchElement) {
      lis.push(elem);
    }
  }
  return lis.length;
};
