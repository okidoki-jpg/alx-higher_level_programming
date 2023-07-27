#!/usr/bin/node

const fs = require('fs');

// Write a string to a file.
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
