#!/usr/bin/node
# script that writes a string to a file
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.log('Usage: node 1-writeme.js <file_path> <content>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`File "${filePath}" has been written.`);
  }
});
