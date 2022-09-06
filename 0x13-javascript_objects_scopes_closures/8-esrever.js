#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    revlist.push(list[i]);
  }
  return revlist;
};
