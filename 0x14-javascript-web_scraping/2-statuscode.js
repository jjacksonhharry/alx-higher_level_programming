#!/usr/bin/node
# script that display the status code of a GET request
const request = require('request');

const url = process.argv[2];

if (!url) {
  console.log('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
