#!/usr/bin/node

const fs = require('fs');

function concatFiles(file1, file2, dest) {
    const data1 = fs.readFileSync(file1);
    const data2 = fs.readFileSync(file2);
    fs.writeFileSync(dest, data1 + data2);
}

concatFiles('fileA', 'fileB', 'fileC');
