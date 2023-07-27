#!/usr/bin/node

const fs = require('fs');

// Read and print the content of a file.
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
