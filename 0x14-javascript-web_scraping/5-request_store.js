#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Make the GET request to the URL
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    // Write the response body to the file
    fs.writeFile(process.argv[3], body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError.message);
      }
    });
  }
});
