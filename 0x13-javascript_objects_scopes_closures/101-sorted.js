#!/usr/bin/node

const { dict } = require('./101-data');

const occurrences = {};
for (const [id, count] of Object.entries(dict)) {
  if (!occurrences[count]) {
    occurrences[count] = [];
  }
  occurrences[count].push(id);
}

console.log(occurrences);
