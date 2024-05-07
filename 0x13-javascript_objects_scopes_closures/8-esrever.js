#!/usr/bin/node
exports.esrever = function (list) {
  let last = list.length - 1;
  let i = 0;

  while ((last - i) > 0) {
    const temp = list[last];
    list[last] = list[i];
    list[i] = temp;
    i++;
    last--;
  }
  return list;
};
