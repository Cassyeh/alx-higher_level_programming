#!/usr/bin/node
const process = require('process');
let length = 2;
while (process.argv[length] !== undefined) {
  length++;
}
if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log(process.argv[2]);
}
