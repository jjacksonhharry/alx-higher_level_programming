#!/usr/bin/node
# script that reads and prints the content of a file.

const fs = require('fs');

try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
